# Hermes Agent — Kaynak ve yürütme rotası

**2026-09-11 / plan v0.15.** Current Work [STATE](STATE.md). Primary `c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`; current upstream doğrulaması değildir.

## Korunan tarihsel kaynak rotaları

[V0.14 tam kaynak defteri](https://github.com/batuhanozgun/agentic-os-search/blob/25b06521083e2a4ddf7b0dbeb9454804796963b6/research/studies/hermes-agent/SOURCE-LEDGER.md) önceki H/T/U01B/W/D/P/U01B2/E/C/V/J/MW/M2/N/UI/A/M3-S/SA/AP/M4/U02 kayıtlarının exact rotasıdır. [SOURCE-LEDGER-THROUGH-V0.9](SOURCE-LEDGER-THROUGH-V0.9.md) ve bütün eski evidence dosyaları yerinde ve değişmeden kalır.

[U02 C01–C18 ve R01/R02](evidence/2026-09-10-turn-lifecycle/SOURCES.md) genel tur/context/session kaynak okumasıdır, runtime deneyi değildir. [M4](evidence/2026-09-10-prompt-restore/SOURCES.md) selected prompt experiment; artificial V04 compression'ın actual sırası değildir. A/SA/AP ortak kaynaklarının örtüşmesi bağımsız doğrulama yapmaz.

## U03 — önceki çalışma, şimdi yayın kurtarması

[17](notes/17-KANBAN-TASK-CLAIM-AND-ACCEPTANCE.md) → **[U03 SOURCES](evidence/2026-09-10-kanban-task/SOURCES.md)** → [RESEARCH](evidence/2026-09-10-kanban-task/RESEARCH.md).

U03-S01 `kanban_db.py` blob `47fdffc353b1fd432acf5929f56463df07b413ad`; S02 connect `9067dfd0e571bc02cb02859c80fb4a551b8f55ce`; S03 dispatch `743e91dbb542132a4981ad9225df49612bc68882`; S04 tools `b776958a55bb5d42ad9c92ec87d6c4ba110f917c`. Bunlar önceki turdaki selected-source kapsamıdır; recovery sırasında yeniden full okunmuş veya çalıştırılmış sayılmaz.

K01–K08 ham kayıt zamanı `2026-09-10T20:06:13.848575+00:00`. [Original evidence tar.xz](evidence/2026-09-10-kanban-task/original-evidence.tar.xz), blob `5484ca39caf7ae5a8f6a31b68caeec0f9a44363d`, 15 özgün dosyayı taşır. Ayrı draft README blob `64533b4183596c3beaee798c4a165cc31a9510f4` değişmeden saklanır. [Manifest](evidence/2026-09-10-kanban-task/RECOVERY-MANIFEST.json) tam member kimliklerini, [RESULT-SUMMARY](evidence/2026-09-10-kanban-task/RESULT-SUMMARY.json) yalnız türetilmiş gezinme görünümünü verir. Exact raw claim için tar içindeki RESULT.json/probe/seçkiler gerekir.

Manuel seçki ve azaltılmış DDL ile gerçek SQLite koşusu; full parent byte/AST sadakati NOT VERIFIED. İlk harness metadata hatası ve corrected run ayrı korunur. Recovery hash/diff/parse kontrolüdür, yeni behavior koşusu değil. Mevcut readable RESEARCH/SOURCES recovery companion'larıdır; tar'da bulunmayan eski prose aynen kurtarılmış diye sunulmaz. [PUBLICATION](evidence/2026-09-10-kanban-task/PUBLICATION.md) bu ayrımı ve önceki final açıklamasının düzeltmesini kaydeder.

## Açık bağımlılıklar

Q07/Q22 actual approval-to-wire ve varyantlar; Q26/Q29 full originals/worker; U03 full-parent fidelity ve actual task/goal/dispatcher/OS/artifact/delivery; gerçek scanner/profiles ve gelecek-task fayda açık. Sentezler yeni bağımsız kaynak değildir. STATE'teki sıradaki teknik çalışma source/phase sınırı korunarak ele alınır.
