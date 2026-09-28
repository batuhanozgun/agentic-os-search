# EXP-006 — Development OS çalışma düzeni

**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini SOUL'un gerektirdiği kabiliyetlerden türetmek.
**Current:** [WORK](WORK.md) v1.8; **P4 / V4 CODEX HEDEF ORTAMI RAPORU HAZIR / P5 KURULUM REHBERİ SIRADAKİ AYRI AŞAMA.** P5 kurulumu ve P6 hedef kabulü yoktur.

## Güncel okuma yolu

AGENT ve gerekli kontrollerden sonra:

1. [STATE](STATE.md) — current, kullanıcı yönü, kanıt ve açık sınırlar.
2. [HANDOFF](HANDOFF.md) — yeni oturumda doğru teslimi devralma.
3. [WORK](WORK.md) — B/S1/P1–P6 bağı, rapor teslimi ve açık hedef kapıları.
4. [DECISIONS](DECISIONS.md) — D027 Codex Environment kararı ve D028 P4→P5 sıralaması dahil kabul edilen kısıtlar.
5. [P4-05 — Codex hedef ortamı revizyonu ve v4 raporu](work/P4-05-codex-environment-revision-v4.md) — Environment değişikliği, resmî Codex/Agents API kaynakları, dosya kimlikleri ve P5 sınırı.
6. **Gerçek `EXP-006_DevOS_v4_Codex_Kaynak_ve_Kanit_Paketi.zip`** — raporun tam gövdesi, v3 baseline, sözleşmeler, kod ve ham QA. Gövdeler GitHub'da değildir; ayrıntılı inceleme için ek veya hash-eşit kaynak gerekir.

V4 kaynak ZIP/PDF/Markdown hash'leri P4-05'tedir. Repository özetinden eksik rapor/kod uydurulmaz. V3 paketi v4 içinde provenance olarak korunur; current hedef değildir.

## Korunan kaynaklar

| Yüzey | Rolü |
|---|---|
| ACTORS.md ve work/P2-01-named-role-contracts.md | İlk aile/rol sözleşmeleri; P3/v2/v3 farklarından bağımsız son kadro değil |
| work/P3-01-work-information-discussion.md | G/Y, içerik–düzen, bakım ve H1–H6 kavramsal bağları |
| work/P4-01-cloud-runtime-and-workspace-design.md | Eski teknik baseline; current mimari veya next-work değil |
| work/P4-02-soul-derived-report-v2.md | Tarihsel v2 teslimi, kaynak kimliği ve sınırlı test kanıtı |
| work/P4-03-unbounded-stress-test-handoff.md | Önceki yarım v3 ve kaynak devri; tarihsel teslim başarısızlığı current değil |
| work/P4-04-unbounded-stress-test-report-v3.md | V3 stres testi/kanıt tabanı; Codex kararından önceki rapor |
| work/P4-05-codex-environment-revision-v4.md | Güncel Codex hedef ortamı revizyonu, v4 teslimi ve P5 geçiş sınırı |
| work/P1-01-claude-cloud-environment-map.md | Tarihsel Claude platform haritası; D027 sonrası current hedef değil |
| sources/U001.md, sources/U002-cloud-plan-and-autonomy.md, EXP-006_Context | Amaç/kısıt/yöntem kaynakları; tarihsel next ifadeleri current sıra değil |
| work/B*.md, work/S1-*.md, history/ | İş/sorumluluk türetimi ve geçmiş; normal devirde körlemesine yeniden yüklenmez |

Kısa cevap çalışma derinliğini küçültmez. Uzunluk, bileşen veya test sayısı bağımsız mimari yeterlik değildir. Current platform kararı Codex'tir; v4 içindeki Agents API topolojisi P5 için teknik blueprint adayıdır. P5 kurulum rehberi ayrı aşamadır; P6/gerçek SOUL işi başlamaz. Agent-control değişmedi.