# EXP-006 — Development OS çalışma düzeni

**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini SOUL'un gerektirdiği kabiliyetlerden türetmek.
**Current:** [WORK](WORK.md) v1.7; **P4 / SAYFA SINIRSIZ V3 RAPOR VE YEREL KANIT TESLİMİ HAZIR / KULLANICI DEĞERLENDİRMESİ BEKLENİYOR.** Mimari kabulü, P5 kurulumu ve P6 hedef kabulü yoktur.

## Güncel okuma yolu

AGENT ve gerekli kontrollerden sonra:

1. [STATE](STATE.md) — current, kullanıcı yönü, kanıt ve açık sınırlar.
2. [HANDOFF](HANDOFF.md) — yeni oturumda doğru teslimi devralma.
3. [WORK](WORK.md) — B/S1/P1–P6 bağı, rapor teslimi ve açık hedef kapıları.
4. [DECISIONS](DECISIONS.md) — kabul edilen kısıtlar; D024 sayfa sınırının kaldırılması, D025 tarihsel devir, D026 bu oturumdaki P4 devamı.
5. [P4-04 — v3 stres testi ve rapor teslimi](work/P4-04-unbounded-stress-test-report-v3.md) — sekiz bulgu, gerçek koşular, kimlikler ve yapılmayanlar.
6. **Gerçek `EXP-006_DevOS_v3_Kaynak_ve_Kanit_Paketi.zip`** — raporun tam gövdesi, sözleşmeler, kod ve ham QA. Gövdeler GitHub'da değildir; ayrıntılı inceleme için ek veya hash-eşit kaynak gerekir.

V3 kaynak ZIP hash'i ve PDF/Markdown kimlikleri P4-04'tedir. Repository özetinden eksik rapor/kod uydurulmaz. `EXP-006_Yeni_Oturum_Devir_Paketi.zip` yalnız v2 tabanlı eski devirdir, yeni v3 değildir.

## Korunan kaynaklar

| Yüzey | Rolü |
|---|---|
| ACTORS.md ve work/P2-01-named-role-contracts.md | İlk aile/rol sözleşmeleri; P3/v2/v3 farklarından bağımsız son kadro değil |
| work/P3-01-work-information-discussion.md | G/Y, içerik–düzen, bakım ve H1–H6 kavramsal bağları |
| work/P4-01-cloud-runtime-and-workspace-design.md | Eski teknik baseline; current mimari veya next-work değil |
| work/P4-02-soul-derived-report-v2.md | Tarihsel v2 teslimi, kaynak kimliği ve sınırlı test kanıtı |
| work/P4-03-unbounded-stress-test-handoff.md | Önceki yarım v3 ve kaynak devri; tarihsel teslim başarısızlığı current değil |
| work/P4-04-unbounded-stress-test-report-v3.md | Güncel v3 rapor/kanıt teslimi ve açık hedef yeterlikleri |
| work/P1-01-claude-cloud-environment-map.md | Tarihsel platform haritası; güncel hedef yeterliği kanıtı değil |
| sources/U001.md, sources/U002-cloud-plan-and-autonomy.md, EXP-006_Context | Amaç/kısıt/yöntem kaynakları; tarihsel next ifadeleri current sıra değil |
| work/B*.md, work/S1-*.md, history/ | İş/sorumluluk türetimi ve geçmiş; normal devirde körlemesine yeniden yüklenmez |

Kısa cevap çalışma derinliğini küçültmez. Uzunluk, bileşen veya test sayısı bağımsız mimari yeterlik değildir. Şimdi kullanıcı P4 v3 sonucunu değerlendirir; açık H kapıları otomatik P5/P6 başlatmaz. Agent-control değişmedi.
