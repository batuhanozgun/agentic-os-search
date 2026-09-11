# Hermes Agent — Açık sorular

**2026-09-11 / plan v0.15.** Q01–Q37 kimlikleri korunur; Q38–Q39 U03 sınırını ekler. [V0.14 exact Q01–Q37 kayıtları](https://github.com/batuhanozgun/agentic-os-search/blob/25b06521083e2a4ddf7b0dbeb9454804796963b6/research/studies/hermes-agent/OPEN-QUESTIONS.md) unchanged inherited questions için ayrıntılı rotadır. Bu yayın kurtarması eski soruları sessizce kapatmaz. [STATE](STATE.md), [SOURCE-LEDGER](SOURCE-LEDGER.md).

## U03 ile değişen ve yeni sorular

| ID | Current disposition |
|---|---|
| Q12 | U02 normal-core modeli + şimdi U03 kalıcı task kaynak/recorded diagnostic eklendi. Bütün HERMES veya recursive coverage hâlâ açık. |
| Q34 | PARTIAL ADVANCE: task/create/dependency/claim/run/complete/block/review gerçek source seçkileri ve K01–K08 arşivi kayıtlı. Transactional task/run/event kabulü, tool-name veya rc=0 değil; actual full dispatcher/worker ve semantic acceptance açık. |
| Q35 | Normal spawn task/run/claim/board kimliklerini taşır; handler expected run ID verir. K03 eski A'nın B'yi kapatmasını seçili consumer'da reddeder. Gerçek process cancellation, tüm caller identity ve gateway/session lease ilişkileri açık. |
| Q36 | K05 commit öncesi rollback ve K06 commit sonrası exception ayrıldı. Task done, caller success, dependent promotion, artifact durability ve delivery acknowledgement birleştirilmiş değil. |
| Q37 | FIRST NEXT TECHNICAL BRIDGE: actual Kanban goal loop hangi run-terminal/superseded koşulunda durur; tool goal gate/judge neyi kabul eder? Ardından goal/loop/heartbeat storage/trigger/continuation farkları. Yalnız yorum ve isim yeterli değildir. |
| Q38 | K seçkilerinin full upstream parent byte/AST sadakati ve init/schema/fixture bağımlılıkları nasıl doğrulanır? Local hashes aktarımı bağlar; source equivalence/whole-runtime ispatı değildir. Güçlü reuse/security kararından önce yeniden açılır. |
| Q39 | Low-level optional expected_run_id operator yolu ile normal worker proof'u bütün caller'larda nasıl ayrılır? K07 düşük seviyeli sınırı çalıştırır; normal worker'ın ID'yi atladığı veya bütün authorization'ın bozuk olduğu sonucu yok. |

Q01–Q11 ve Q13–Q33'ün v0.14 disposition'ları değişmez. Özellikle Q07/Q22 ordinary compaction→API-message source bağlantısı kurulmuştur fakat final wire/timing/all variants açık; Q26/Q29 full-original/full-worker verifier NOT RUN. Review/skill/ledger/sync/quality ve eski memory/approval sınırları terk edilmedi.

## Recovery ile yeni kanıtı ayır

[U03 result summary](evidence/2026-09-10-kanban-task/RESULT-SUMMARY.json) eski kayıtlı koşudan türemiştir; tam snapshots/mutants [original archive](evidence/2026-09-10-kanban-task/original-evidence.tar.xz) içindedir. Bu tur yeni probe çalıştırılmadı. Archived record, transfer identity, source fidelity ve bağımsız behavioral/semantic doğrulama ayrı düzeylerdir.

İlk harness metadata failure'ı kaynak ürün hatası değildir; ilk görünmeyen case sonuçları sayılmaz. Sekiz ana durumda matched ve üç negatif kontrol recorded olsa da full parent/actual app/worker/provider/OS/artifact/judge/delivery eksikleri kapanmaz. Aynı dar suite'i çoğaltmak coverage değildir.

Yayın kurtarması known U03 two-blob kapsamını kapatır; bütün geçmiş sohbet dosyalarının evrensel envanteri yapıldığı iddia edilmez. Kurulum/provider/credential/upstream/control/Foundation/adoption yetkisi değişmedi.
