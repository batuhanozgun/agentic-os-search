# EXP-006 — Development OS çalışma düzeni

**Üst amaç:** SOUL'u geliştirecek ekibin çalışma düzenini SOUL'un gerektirdiği kabiliyetlerden türetmek.
**Current:** [WORK](WORK.md) v1.6; **P4 / SAYFA SINIRSIZ STRES TESTİ VE RAPOR v3 / YARIM KALDI / YENİ OTURUM İÇİN DURAKLATILDI.** V2 son doğrulanabilir dosya tabanıdır; yeni v3 raporu/test sonucu teslim edilmiş değildir. P5 kurulumu veya P6 hedef kabulü yoktur.

## Güncel okuma yolu

AGENT ve gerekli kontrollerden sonra:

1. [STATE](STATE.md) — current, son kullanıcı yönü, doğrulanmış/doğrulanmamış durum ve durma sınırı.
2. [HANDOFF](HANDOFF.md) — eski konuşmayı görmeden yarım çalışmayı devralma.
3. [WORK](WORK.md) — B/S1/P1–P6 bağı ve sayfa sınırsız P4 işi.
4. [DECISIONS](DECISIONS.md) — kabul edilen kısıtlar; D023–D025 rapor yeniden yazımı, sayfa sınırının kaldırılması ve oturum devri.
5. [P4-03 — stres testi ve yeni oturum devri](work/P4-03-unbounded-stress-test-handoff.md) — kaynak kimlikleri, dört doğrulanmamış ipucu, erişim sınırı ve devam planı.
6. [P4-02 — v2 teslimat kaydı](work/P4-02-soul-derived-report-v2.md) — son tamamlanmış raporun provenance ve kanıt kapsamı; kendi tarihsel next'i current değildir.
7. **Gerçek v2 kaynak ZIP/PDF veya yeni oturum devir paketi** — raporun tam gövdesi, sözleşmeler, model ve tarihsel QA. Bu dosyaların tamamı GitHub'da değildir; ek yoksa özetten rapor incelemesi yapılmaz.

`EXP-006_Yeni_Oturum_Devir_Paketi.zip`, v2 kaynaklarıyla yarım v3 devrini birlikte taşır. Yeni rapor değildir. Yeni oturumdaki devam komutuyla aktif iş P4 stres testi/yeniden yazım olarak sürer; v2'den doğrudan P5'e geçilmez.

## Korunan kaynaklar

| Yüzey | Rolü |
|---|---|
| ACTORS.md ve work/P2-01-named-role-contracts.md | İlk aile/rol sözleşmeleri; P3/v2 farklarından bağımsız son kadro değil |
| work/P3-01-work-information-discussion.md | G/Y, içerik–düzen, bakım ve H1–H6 kavramsal bağları |
| work/P4-01-cloud-runtime-and-workspace-design.md | Eski teknik baseline; current mimari veya next-work değil |
| work/P4-02-soul-derived-report-v2.md | Tarihsel v2 teslimat, yeni mimari öneri ve sınırlı test kaydı |
| work/P4-03-unbounded-stress-test-handoff.md | Aktif sayfa sınırsız stres testi/yeniden yazımın devir kaydı |
| work/P1-01-claude-cloud-environment-map.md | Tarihsel platform haritası; güncel hedef yeterliği kanıtı değil |
| sources/U001.md, sources/U002-cloud-plan-and-autonomy.md, EXP-006_Context | Amaç/kısıt/yöntem kaynakları; tarihsel next ifadeleri current sıra değil |
| work/B*.md, work/S1-*.md, history/ | İş/sorumluluk türetimi ve geçmiş; normal devirde körlemesine yeniden yüklenmez |

Kısa kullanıcı cevabı çalışma derinliğini küçültmez. Gerekli kalite sayfa sayısına veya kolay uygulamaya feda edilmez. Aynı şekilde uzun rapor, çok bileşen veya geçen unit test bağımsız mimari yeterlik kanıtı değildir. Agent-control değişmedi.
