# soul — okuma defteri

Repo: `batuhanozgun/soul`  
Rol: SOUL'un current explicit intent'i + Development OS'nin birincil kuruluş/işletim kanıtı  
Okuma stratejisi: `main` intent anchor → yüksek-bilgi çalışma dalı → foundation → ilk work/verification → yalnız gerekli sonraki kanıt

## Düzeltme: repo yalnız `main` değildir

İlk okumada default `main` dalında yalnız `README.md` görülmüş ve repo küçük kabul edilmişti. Bu hüküm yalnız `main` görünümü için doğrudur.

Dal taraması sonrasında çok sayıda `work/*`, `verify/*`, `review/*`, `audit/*` ve özellikle `phase0/development-os` dalı bulundu. Bu nedenle SOUL artık yalnız explicit-intent anchor değil, SOUL'un kendi geliştirme işletim sistemine dair **birincil araştırma kaynağıdır**.

## Okuma kaydı — `main`

| Kaynak | SHA / commit | Tür | Maddi bulgu |
|---|---|---|---|
| `README.md` | `9dbded30` | full | SOUL first principles'tan genel amaçlı agentic architecture olarak yeniden kuruluyor; intended outcome → controlled, verifiable working system; `development/` ile `system/` ayrı; ilk paket Development OS |
| bootstrap commit | `7b2a9a4` | full diff | 2026-08-25'te yalnız README ile bilinçli yeniden başlangıç |

## Okuma kaydı — `phase0/development-os`

### Development OS amacı

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `development/README.md` | `e6a87f70` | full | SOUL geliştirmesini session length/context loss/model memory/single-model self-evaluation/undocumented decisions/unverified output'tan bağımsızlaştırmak; fresh session repo state'inden cold-start edip bounded work + evidence + handoff yapabilmeli |
| `development/00_foundation/VISION.md` | current branch | full | SOUL preset workflow/team/template değil; intended outcome için gereken çalışma sistemini kurabilen general-purpose agentic system |
| `development/00_foundation/DEFINITION.md` | current branch | full | SOUL'un işi `system formation`: outcome'u anla → gereken sistemi belirle → capability'leri kur/organize et → işlet → doğrula → adapt et → continuity/governance/state'i koru |
| `development/00_foundation/NON_NEGOTIABLES.md` | current branch | full | outcome-first, least privilege, independent verification, evidence-before-closure, explicit external state, governed capability acquisition, repair/adaptation, no hidden owner orchestration, fail-visible, scale-appropriate control, durable traceability |
| `development/00_foundation/SUCCESS_CRITERIA.md` | current branch | full | cold-session reconstructability, governance-before-product architecture, failed verification blocks closure, unresolved decisions visible, missing capability governance, recovery/adaptation, low hidden-owner orchestration, unbounded governance growth yok |

### İlk work/verification zinciri

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `development/04_work/WP-000-DEVELOPMENT-OS.md` | `6f5042ec` | full | Amaç: SOUL'u uzun fresh-session'larda tek chat/model memory/producer self-certification'a bağlı olmadan tasarlayacak durable repo OS. Açık problem: böyle bir disiplin kurulmazsa SOUL, kontrol etmeyi hedeflediği aynı agentic failure class'ları kendi geliştirmesinde yeniden üretir. KEEL klasörlerini yeni sisteme map etmek ve ürün mimarisi Phase 0 non-scope |
| `development/04_work/WP-001-PHASE0-VERIFICATION.md` | `5f0b5bf3` | full | fresh verifier WP-000'ı exact commit'e karşı bağımsız değerlendirmekle görevli; verifier repair yapamaz; tarihsel sonuç `FAIL` |
| `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md` | `d95f4507` | full | İlk gerçek verification iki kusurla FAIL: cold-start mandatory read-order'ları birbirini tutmuyor; `NEXT_SESSION.md` current WP bilgisini stale duplicate olarak taşıyor. 9/11 criterion PASS olsa da criterion 1–2 FAIL olduğu için overall FAIL korunmuş |

### Öncül repoların SOUL'a açık aktarımı

| Kaynak | SHA | Tür | Maddi bulgu |
|---|---|---|---|
| `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md` | `fa9b281e` | full | KEEL-Work, keel-dev, oyun2, os-architect ve keel-research kaynakları SHA'larıyla okunmuş; source-derived principles ile SOUL-specific synthesis decisions ayrı tutulmuş |

Bu synthesis'in doğrudan taşıdığı tekrar eden ilkeler:

1. project truth chat/model memory dışında yaşar;
2. objective/method/state/evidence/decision authority ayrılır;
3. observation/inference/assumption/verified result ayrılır;
4. producer confidence/tool success/repeated-model agreement/retrieved content proof değildir;
5. mevcut plan/mekanizma/tool ayrıcalıklı default değil, hipotezdir;
6. material architecture framing/necessity/alternative-layer/falsification testinden geçer;
7. owner value/scope ile teknik araştırılabilir karar ayrılır;
8. failure'da hem immediate defect hem neden anticipate/prevent/detect edilemediği incelenir;
9. mümkünse öğüt yerine observable trace/mechanical control;
10. risk/ambiguity/novelty/irreversibility ile orantılı derin reasoning;
11. independent verification + exact-target freshness;
12. decision-relevant rationale/evidence kaydedilir, private chain-of-thought istenmez.

SOUL'a özgü synthesis bunları mekanik olarak kopyalamıyor; tek canonical reasoning policy, tek cold-start sequencing authority, trigger-based deeper checks ve architecture/failure/provenance kontrolleri gibi yeni tasarım seçimlerine dönüştürüyor.

## Şu anda doğrudan söylenebilenler

### SOUL ürününün amacı — BİRİNCİL KAYNAKLA DOĞRULANDI

SOUL'un hedefi bir workflow şablonu veya KEEL'in genel sürümü değildir. Kullanıcının intended outcome'unu alıp **o hedef için gereken kontrollü çalışma sistemini oluşturabilen, işletebilen, doğrulayabilen ve gerçeklik değiştiğinde adapte edebilen genel amaçlı agentic operating architecture** olmaktır.

### Development OS'nin amacı — BİRİNCİL KAYNAKLA DOĞRULANDI

SOUL'u tasarlama süreci, SOUL'un çözmeye çalıştığı failure class'ları kendi içinde yeniden üretmemelidir. Bu nedenle ürün mimarisinden önce repo-authoritative, cold-startable, bounded, independently verified, fail-visible bir development operating system kuruluyor.

### Tarihsel öncüllerle bağ — BİRİNCİL KAYNAKLA DOĞRULANDI

SOUL Phase 0 kendi evidence dosyasında KEEL/os-architect ve diğer öncül alanlardan hangi reasoning/governance ilkelerini aldığını SHA seviyesinde belgeliyor. Bu nedenle bağ yalnız benzerlik veya tarih sırası değil.

## Açık sorular

- SOUL Research projesi, SOUL product development'ın hangi araştırma boşluğunu doldurmak için ayrı tutuluyor?
- `phase0/development-os` içinde sonraki reasoning/adversarial work packages hangi yeni failure class'ları açtı?
- First-principles general-purpose hedefi KEEL'in yazılım-projesi bağlamından hangi capability/failure architecture araştırmalarını gerektiriyor?
- Development OS'nin kendisi Phase 0'da neden bu kadar çok repair/reverification turuna ihtiyaç duydu; bunlar SOUL Research için hangi meta-gereksinimleri doğuruyor?

## Sonraki okuma

Geniş dal tüketimi yapılmayacak. En yüksek bilgi değeri sırası:

1. Phase 0'ın reasoning-policy ve adversarial-review paketlerinden yalnız yeni failure class üreten kayıtlar;
2. SOUL Research ile product-development arasındaki sınırı açıklayan work/evidence kayıtları;
3. daha sonra capability/failure architecture work package'ları — ancak araştırma niyeti için gerçekten gerekli olursa.
