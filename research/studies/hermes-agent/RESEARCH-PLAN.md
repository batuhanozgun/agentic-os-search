# Hermes Agent — Araştırma planı

**v0.12 / 2026-09-10.** AP tesliminin özgün kaydı ve kullanıcı tarafından kabul edilmiş kapsam değerlendirmesi. Yeni teknik deney bu checkpoint'te yok. İş yetkisi [STATE](STATE.md), yöntem/kapanış [METHOD](METHOD.md). [v0.11 tam plan](https://github.com/batuhanozgun/agentic-os-search/blob/634ab66f195130d551d58dfc062639e0feec23fa/research/studies/hermes-agent/RESEARCH-PLAN.md) tarihçeyi korur.

## Amaç ve karar

Önce HERMES-native model, sonra dört alan ve SOUL/Development OS. Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; W belgeleri unpinned. Not/koşu/yayın sayısı olgunluk ölçüsü değildir. AP, UI/A ve M3-S/SA ayrı arşivlerdir; aynı modül üç bağımsız kanıt kaynağı olmaz.

Seçilen sıra: AP arşiv kapanışı → bounded visibility köprüsü → geçici alt-sistem sentezi → geniş topoloji/omission kontrolü. [SCOPE-REVIEW](inventory/SCOPE-REVIEW-2026-09-10.md) alternatifleri, gerekçeyi ve çıkış şartlarını taşır. Genel kapsamı U01'in bütün residual'ları kapanana kadar erteleme.

## Aile kapsamı

| ID | Aile | Mevcut düzey / açık iş |
|---|---|---|
| F01 | Başlama/araç döngüsü/retry/kesinti | Seçili facade/round/worker/ingress; genel lifecycle tamamlanmadı. |
| F02 | Context/prompt/schema/compression/cache | Memory/store ve UI source bağı; **ilk iş approval→stored/cached prompt→prepared request**. |
| F03 | Session/lineage/search/repair | Seçili persist/wire; arama/restore/DB yaşam döngüsü açık. |
| F04 | Memory/skill/ownership/approval/rollback/sync | En derin kesit; N ve skill bounded probes var. Ledger/sync/reuse köprüleri açık. |
| F05 | Provider/credential/profile/config | Profile/transport ve supplied config kaynağı; genel resolver/config lifecycle açık. |
| F06 | Tool/skill/plugin/MCP/authority | Selected worker/middleware ve A/SA/AP; tam Q26 açık. |
| F07 | Backend/native effect boundary | İlk topoloji ve source referansları; geniş açıklama yok. |
| F08 | Delegation/cancel/worktree/writers | Seçili cancel/busy/worker; çok-yazar ve lifecycle açık. |
| F09 | Gateway/auth/session/delivery | Normal onay yolunda derin; bütün platformlar/teslim açık. |
| F10 | Cron/proaktif iş/queue/restart | Curator referansları; scheduler ve report bağı açık. |
| F11 | CLI/TUI/desktop/web/API/ACP | Normal CLI/gateway pending; diğer yüzeyler açık. |
| F12 | Install/update/compat/tests/evals | Dar deneyler; genel dağıtım/eval/kalite açıklaması açık. |

A0 pin/yöntem kurulu; A1 topoloji kısmi. B0 mekanizma notları derin fakat tam aile kapanışı yok. Native alt-sistem/genel ilişkiler/dört-alan/CORE henüz tamamlanmadı. Provisional aileler nihai sistem ontolojisi değildir.

## Şimdiki sınırlı birim: U01-M4 visibility

Soru: normal memory approve sonrası mevcut CLI ve cached gateway ajanında hangi görünüm ne zaman değişir?

İlk source `_restore_or_build_system_prompt`; ardından system_prompt invalidation/build ve turn context; cache reuse/eviction ve compression/keep-prompt çağırıcıları. Kaynak caller ilişkisini göstermeden sentetik kodla ürün sonucu çıkarma.

Ayrı durumlar: pending payload, kalıcı dosya, live store, frozen snapshot, DB stored prompt, cached prompt, prepared messages/request. Onay-mode config değişimi payload approve değildir. Her-tur reload, koşullu refresh, yeni store+eski DB prompt ve gateway/CLI nesne ömrü rakip açıklamalar olarak sınanır.

Önce kaynak; ardından mümkünse provider'sız offline ölçüm. Gerçek upstream modül, selected definition ve fake DB/caller ayrılır. Normal yazı/silme/hata/restore örneklerinin hangileri gerçekten yürütüldüyse o kadar iddia edilir. Yanlış durumda kırmızı veren karşı kontrol aranır. Test sayısı kota değildir.

Çıkış: ilgili koşullarda hangi geçişin görünümü yenilediğini açıklayabilmek veya tam engelli halkayı kaydetmek. Full outbound request yakalanamadıysa selected prompt testi onun yerine sunulmaz. Kurulum/credential/provider sınırı genişletilmez.

## Sonraki birimler

İlk ara sentez: review/curator önerisi → onay/yetki → değişiklik → görünürlük/reuse → maintenance/rollback; kenarlar kaynak/koşu/çıkarım/açık olarak ayrılır. Bu geçici model mevcut birikimi okunabilir kılar; öğrenme faydasını veya bütün HERMES'i doğrulamaz.

Sentezden sonra geniş kaynak-topoloji kontrolü: genel work/context/session çekirdeği; tool/provider/backend/delegation; gateway/cron; apps/install/eval. Hangi eksik aile geçici açıklamayı değiştirebilir? Listeleme ve full-read karıştırılmaz. Ledger/backup/restore/sync → skill-cache → curator nested batch/report/cron köprüleri bu karşı okuma ile bağlanır.

Q26/Q29 tam-runtime, actual UI faults, bütün auth/profile/hook ve scanner/kalite ileri doğrulamasıdır. Yeni exact materyalizasyon, source değişimi veya load-bearing kullanım olmadıkça eski A/SA/AP/N/C/V fixture'ları tekrarlayıp bütün çalışmayı bunlara kilitleme. E01/E02 legacy full-original verifier NOT RUN kalır.

## Yayın disiplini

14/AP + original 15 dosya + transfer check yeni; önceki notes/evidence değişmez. Current routers ve katalog aynı checkpoint'i taşır. Non-force main ve content readback gerekir. Bitiş ölçütü METHOD; ayrı AP aktarımı yeni araştırma başarısı diye sayılmaz.
