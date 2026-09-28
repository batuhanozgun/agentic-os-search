# EXP-006 — HANDOFF

**28 Eylül 2026 / P4 v4 Codex hedef ortamı raporu hazır / P5 Codex kurulum rehberi sıradaki ayrı aşama.**

## 1. Ne devralınıyor?

V3 stres testi/kanıt tesliminden sonra kullanıcı DevOS'un hedef Environment kararını **Codex** olarak değiştirdi. Önce dokümanın buna göre yeniden hazırlanmasını, ardından P5 kurulum rehberinin Codex'e göre hazırlanmasını istedi. V4 bu Environment transition'ını işler; P5 kurulumu değildir.

Claude Code cloud kararı D011'de tarihsel kalır. D027 current platform kararını Codex'e geçirir; D028 P4 v4 doküman → P5 rehber sırasını taşır. SOUL'un ilk gerçek işi hâlâ DevOS ekibi tarafından keşfedilecektir; assistant hazır backlog seçmez.

## 2. Güncel kaynak ve giriş

AGENT ve gerekli kontroller → INDEX → STATE → WORK → DECISIONS → **[P4-05](work/P4-05-codex-environment-revision-v4.md)** → gerçek v4 kaynak paketi.

`EXP-006_DevOS_v4_Codex_Kaynak_ve_Kanit_Paketi.zip`, 3638865 byte; SHA-256 `df895557d77c4585627615010ac5061cde95ce768f73cfdea59259d1e5726aff`.

PDF `EXP-006_DevOS_v4_Codex_Hedefli_Rapor.pdf` hash'i `cd60f7fde9e1ba4fe7f1ecc7f2abb0b008e57bc12868d51721d6442f17c2e425`; Markdown `EXP-006_DevOS_v4.md` hash'i `22f4660d16b487f5a35a3a9eecff1e65246efc53707f93ce50d99b3d3dc9f146`.

Tam gövdeler repository'ye yüklenmedi. V4 paket, exact v3 kaynak paketini `baseline-v3/` altında ve v2 baseline'ı ayrıca taşır. Yeni oturumda ayrıntılı rapor/kod işi için gerçek v4 paket veya hash-eşit kaynak gerekir.

## 3. V4 neyi değiştirdi?

Genel DevOS omurgası korunur: Work keşfi/RPD, rol–agent–principal ayrımı, K1/K2, bilgi/memory/context, typed relations, protected effect, publication/recovery, uzun ürün ve yöntem aktarımı.

Environment-bound yüzey değişti. Güncel OpenAI resmî kaynaklarına göre v4, **Agents API managed Codex harness**'ını P5 için birincil teknik blueprint adayı yapar; root/subagent orkestrasyonu ve başlangıç execution seçeneği olarak OpenAI-hosted sandbox'ı önerir. `self_hosted`, protected credential/tool boundary, PostgreSQL/publisher ve exact persistence/topology P5 qualification konusudur. Bu teknik öneri Codex kullanıcı kararıyla aynı statüde değildir.

Session, environment ve Work state eşitlenmez. Session environment'tan uzun yaşayabilir; replacement compute eski dosyaları otomatik geri getirmez; turn completion tool başarısını tek başına kanıtlamaz. Bu nedenle canonical Work/Request/Contribution/effect observation DevOS'un dayanıklı yüzeyinde kalır.

## 4. Kanıt ve açık yükler

V3 mekanik tabanı v4 çalışma kopyasında yeniden koşuldu: v2 baseline 40 test/dört guard; sekiz scoped karşı örnek; 53 candidate test; sekiz mutation içinde yedi assertion/tek downstream error ayrımı. Bunlar Codex-native test değildir.

V4 PDF 51 sayfa ve 675/675 metin birimi QA'sından geçti. Actual Agents API account/session, root/subagent K1/K2, OpenAI-hosted/self-hosted environment, credential brokering, PostgreSQL, protected publisher, restore ve G01/G02/G04/G05/G06/G07 gerçek yeterliği açıktır.

## 5. Sonraki sorumluluk

**Şimdi kullanıcıya v4 P4 dokümanı teslim edilir ve bu tur durur.** Sonraki ayrı çalışma **P5 Codex kurulum rehberi**dir. P5; actual Agents API/environment/tool/persistence seçimlerini adım adım kurulabilir runbook'a dönüştürmeli ve H-ENV/H-K1-K2/H-AUTH qualification'ını kurulumla birlikte planlamalıdır.

P5'in sıradaki çalışma olması, kurulmuş olduğu veya P6 kabulüne geçildiği anlamına gelmez. P6 ve ilk gerçek SOUL backlog'u başlamaz.
