# EXP-006 — STATE

**Durum:** AÇIK / P4 v4 Codex hedef ortamı raporu hazır / P5 kurulum rehberi sıradaki ayrı aşama.
**Güncelleme:** 28 Eylül 2026. **Üst plan:** [WORK](WORK.md) v1.8.
**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini SOUL'un gerektirdiği gerçek kabiliyetlerden türetmek.
**Current:** [P4-05 — Codex hedef ortamı revizyonu ve v4 raporu](work/P4-05-codex-environment-revision-v4.md). V4 rapor teslimi tamamlandı; P5 kurulum rehberi henüz üretilmedi/uygulanmadı ve P6 hedef kabulü yapılmadı.

## Son kullanıcı yönü ve karşılığı

Kullanıcı DevOS'u yaratacak hedef yapının **Codex** olmasına karar verdi; önce raporun bu karara göre yeniden hazırlanmasını, ardından P5 kurulum rehberinin Codex'e göre hazırlanmasını istedi. D027 current Environment kararını Claude Code cloud'dan Codex'e geçirir; D011 tarihsel karar olarak korunur fakat current değildir. D028 sıralamayı P4 v4 rapor revizyonu → P5 kurulum rehberi olarak sabitler.

V4, v3'ün sekiz scoped bulgusunu ve yerel mekanik kanıtını korur; Environment/topoloji, session/subagent, identity/secret ve recovery bölümlerini güncel OpenAI resmî Codex/Agents API yüzeylerine göre yeniden bağlar. Agents API P5 için birincil teknik blueprint adayıdır; `openai_hosted` / `self_hosted`, protected effect, persistence ve exact subagent topolojisi P5 qualification konusudur. Bu teknik yorum kullanıcı tarafından ayrı bir “Agents API dışında Codex kullanılamaz” kararı değildir.

## Doğrudan gözlenen ve açık kalan

Sekiz sınırlı v2 karşı örneği yeniden üretildi; eski dört ipucu bunların içindedir. V2'nin 40 testi/dört guard deneyi ayrıca yeniden koşuldu. V3 yerel modelinde 53 test geçti. Sekiz yeni bozmanın yedisi hedefli assertion, biri sonraki KeyError ile sonuçlandı; ikincisi eşdeğer doğrulama sayılmadı. Kod/sözleşme farkları ve düzeltme sınırları P4-04'te.

Yerel Python/SQLite ve geçici bare Git koşuları v4 çalışma kopyasında yeniden geçti. Gerçek Codex Agents API session/subagent akışı, seçilecek OpenAI-hosted/self-hosted environment, PostgreSQL, bağımsız güvence, korunan principal/publication, dağıtık restore ve SOUL bilişsel yeterliği **açıktır**. On iki senaryo masa başıdır. Tasarım önerisi, resmî platform kabiliyeti, yerel kod ve actual hedef davranış aynı kanıt değildir.

V4 PDF 51 sayfa; 675/675 beklenen metin birimi, glif/geometri/dahili bağlantı kontrolü geçti ve seçili yüksek-bilgi sayfaları görsel incelendi. V3 ortak modelinde 53 test yeniden geçti; sekiz mutation deneyi yedi assertion/tek downstream error ayrımıyla aynı sınırı korudu. Bu kontroller Codex-native qualification değildir.

## Gerçek kaynak erişimi

Güncel kaynak: **`EXP-006_DevOS_v4_Codex_Kaynak_ve_Kanit_Paketi.zip`**, 3638865 byte; SHA-256 `df895557d77c4585627615010ac5061cde95ce768f73cfdea59259d1e5726aff`.

PDF: `EXP-006_DevOS_v4_Codex_Hedefli_Rapor.pdf`, SHA-256 `cd60f7fde9e1ba4fe7f1ecc7f2abb0b008e57bc12868d51721d6442f17c2e425`. Düzenlenebilir Markdown: `EXP-006_DevOS_v4.md`, SHA-256 `22f4660d16b487f5a35a3a9eecff1e65246efc53707f93ce50d99b3d3dc9f146`.

Tam rapor/kod konuşma teslim eklerindedir; repository P4-05 ve devam durumunu taşır, ZIP'nin tam gövdesini değil. V4 paketi ayrıca exact v3 kaynak ZIP/gövdesini provenance için `baseline-v3/` altında korur. Yeni oturumda ayrıntılı inceleme için gerçek v4 paket veya hash-eşit kaynak gerekir.

## Korunan sınırlar

Codex hedef Environment kararı, K1 talep→çalışma→yanıt→kullanım, K2 rutin geçişlerde Batu'nun taşıyıcı/tetikleyici olmaması, gerçek insan müdahalesi/yetki/kabul, G/Y ve D021 içerik–düzen sahipliği korunur. SOUL'un ilk ve sonraki gerçek işlerini ekip keşfeder; assistant hazır backlog seçmez. Rol sayısı agent/subagent sayısı değildir. V4 içindeki Agents API/openai_hosted default blueprint'i teknik öneridir; Codex kararıyla aynı epistemik statüde değildir.

## Current devam

AGENT ve gerekli kontroller → [INDEX](INDEX.md) → STATE → [HANDOFF](HANDOFF.md) → WORK → DECISIONS → **[P4-05](work/P4-05-codex-environment-revision-v4.md)** → gerçek v4 kaynak paketi. P4-04 v3 stres testi/kanıt tabanı, P4-03 eski devir, P4-02 v2 provenance ve P4-01 eski baseline'dır.

**Bu turun durma noktası:** Codex'e göre yeniden hazırlanmış P4 v4 dokümanını kullanıcıya teslim etmek. **Sıradaki ayrı çalışma:** P5 Codex kurulum rehberi. Rehber actual Agents API/environment/tool/persistence kararlarını somutlaştıracak; bu turda P5 kurulmuş veya doğrulanmış sayılmaz. P6 ve gerçek SOUL backlog'u başlamaz.
