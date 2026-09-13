# Hermes Agent — STATE

**2026-09-13 / U14 / plan v0.27 — INSTALLATION, UPDATE AND ACTIVATION.**
**Statü:** ACTIVE PARTIAL RESEARCH; HERMES bütünü tamamlanmadı. Q58 normal install/update ve refusal/recovery kaynak açıklaması ilerledi; gerçek kurulum/güvenilirlik/kalite kapanışı değildir.
**Primary:** `NousResearch/hermes-agent@c4a5deeffa959f8ebc891e02c5bcf767aff1dd2a`, manifest0.21.0; current release veya kurulu binary değil.
**Yayın authority:** [U14 PUBLICATION](evidence/2026-09-13-install-update/PUBLICATION.md). Bu başlık actual main/ref/readback yerine geçmez. [PLAN](RESEARCH-PLAN.md), [METHOD](METHOD.md), [INDEX](INDEX.md), [META](META.md).

## Amaç, yetki ve devralınan güncel durum

Kullanıcının “anladım. plana göre devam et. operasyonel sınırına kadar çalış.” talebi güncel repo ile yorumlandı. Amaç önce HERMES-native mekanizma/alt-sistem/ilişkiler, sonra CORE ve ayrı daha-geç dört-alan/SOUL/Development OS aday değerlendirmesidir. Araştırma canlı ürün değişimi veya adoption yetkisi değildir.

İlk main **93d6b14438802163ed3f542beded218e14cc51cf**, eski sohbetin U12 açıklamasından ileride U13/Q57'yi taşıyordu. U13 source ve manuel seçki diagnostic tekrarlanmadı. Final routes yayımlı fakat makbuzu stale idi: **40a7f952f04b893b2dd0ffdb3df551adfca75c4a** yalnız U13 PUBLICATION'ı uzlaştırdı; actual main/ref, tek-path compare ve yeni metin geri okundu. Eski prepared metni tarihsel olarak korunur. [U13 makbuzu](evidence/2026-09-13-delegation-reentry/PUBLICATION.md).

Yalnız `research/studies/hermes-agent/**` ve CATALOG HERMES satırı değişebilir. Foundation, context/Codex, AGENT/agent-control, diğer studies, upstream, architecture/adoption, izin/credential ayarları değişmez. Canlı installer/updater veya service, gerçek user home/credential, model/provider/NAS/native backend koşusu yoktur. Otomatik/background devam yoktur.

## Gerçek incremental kapılar

Q58 opening **1d65fd3e701dcd7c3c84b7efebb99666ca9377e0**, yalnız PLAN; actual main/ref/tam metin/tek-path compare sonrası A başladı.

A **c0d6418817e512137567e32c8d5aeabdb006f8f3**, rootb560a42c97b73a8b26c67383d5612bfa68911567: iki yeni evidence+STATE. Nonforce main/ref ve üç tam metin geri okunduktan sonra B başladı.

B **2ce9310ad237bfaebcdbcc26ed5fc333f98b54ba**, root5d4a955469f375d81b51a59a26332c5c804bd0b9: üç yeni evidence+STATE. Actual main/ref, dört-path compare ve B1–48/49–EOF, B kaynakları, NOT RUN ve STATE tam geri okundu. Sonra current routes ve sonraki soru uzlaştırıldı. Bunların gerçek final yayın sonucu PUBLICATION'da tutulur.

**Kayıt kapısı sürer:** bir büyük kaynak/kanıt/sınır/sonraki soru dilimi main'e bağlanıp doğrulanmadan ikincisi biriktirilmez. Erişim engelinde mevcut dilim çözülür. Küçük metin yayını gelecekteki bütün/binary yazmaların garantisi değildir.

## U14'te gerçekten ilerleyen

[Note29](notes/29-INSTALLATION-UPDATE-AND-ACTIVATION.md)→[A](evidence/2026-09-13-install-update/INSTALL-AND-ACTIVATION.md) + [B](evidence/2026-09-13-install-update/UPDATE-AND-RECOVERY.md). [A S01–S06](evidence/2026-09-13-install-update/INSTALL-SOURCES.md) ve [B S07–S14/S05 ekleri](evidence/2026-09-13-install-update/UPDATE-SOURCES.md) gerçek full/selected okuma kapsamını taşır.

A kaynak/build/layout/ref/dependency/shim/profile/config/activation; B install-method authority/backup/checkout/dependency-recovery/fleet/receipt zinciridir. Effective HEAD, installed graph, user state ve active process ayrı; core/lazy/fleet yükümlülükleri ayrı; update lock ve recovery lock aynı atomik claim değildir. Restart komutundan sonra actual consumer runtime identity ve beklenen replacement'ı kontrol edebilir. Backup/probe grace ve banner/exit/receipt sınırları genellenmez.

**Yeni behavioral execution: YOK.** HERMES modülü, installer/updater, package manager, DB, service, model/provider veya upstream suite çalıştırılmadı. No RESULT/PASS. FULL READ local byte/dependency/OS doğrulaması değildir. Koşullu iki updater kabulü, partial/success ayrışması veya failed receipt write kaynak çıkarımıdır; gerçek yarış/yanlış update/data-loss gözlemi değil. [NOT RUN](evidence/2026-09-13-install-update/CHECKS-NOT-RUN.md).

## İlk sonraki geniş kaynak sorusu — Q59

**Skill-library lifecycle:** install/update/startup sync→bundled/user/agent-created origin ve manifest/ledger→user edit/deletion/relocation/restore→sonraki skill keşfi/tüketimi. Başlangıç gerçek çağıranlar: `scripts/install.sh` skill sync, `hermes_cli/main.py` startup skill sync, `hermes_cli/update_cmd_maint.py` bundled/profile sync; sonra `tools/skills_sync.py` ve actual manifest/ledger/skill-discovery consumer'ları. Curator aynı yaşamda bounded alt bağdır; tüm multi-agent kalite veya bütün UI ekosistemi kapsam değildir.

Gerekçe: [U13 coverage](inventory/SCOPE-REVIEW-2026-09-13-U13.md) F12 install/update ile F04 library yaşamı ve eval/quality'yi karşılaştırdı. Q58 artık anlamlı normal ve farklı değişim yollarını açıklar; update'in gerçekten beceri kütüphanesine dokunduğu görüldü. F04'ün eski derin proposal/approval araştırması tekrarlanmayacak; onun operasyonel dağıtım/sync/restore/sonraki kullanım bağı açılacak. Eval/future-task quality kaybolmaz. Q59 bu tur araştırılmadı; current planın ilk sonraki kaynak işidir. Mimari/implementation aşaması başlamaz.

## Korunan araştırma ve residual'lar

Q58 all-platform/build/assets/full solver/custom-home/profile/config/provenance authority, actual mutex/repair/snapshot/DB/fleet/receipt/first request açık. Bütün fault matrisini tüketmek geniş araştırmanın ön koşulu değildir; karşı kanıt veya güçlü reliability/adoption reuse exact doğrulamayı yeniden açar. Erteleme kapanış değil.

Q57 source/manual diagnostic full-parent fidelity, actual claim/ack/expiry/crash/queue/TUI/adapter/request değildir. Q54 tool/child/context/workspace/cancel; Q55 native binding/history; Q56 terminal/persistence/control; Q40/Q42 actual DB/quiet/startup; Q47 timing/store; Q48/Q50 transport/cancel; U10 Q49/Q51/Q52 ve eski Q07/Q22/Q26/Q29/Q38 quality/fidelity açık.

METHOD, notes01–28, U04–U13 özgün research/diagnostic/raw ve synthesis01–04 değiştirilmez. U13 PUBLICATION uzlaştırması özgün teknik kanıtı değiştirmedi. U14 A/B metinleri final routes sırasında değişmez. U04-A/18 ile U04-B/19 ayrı; B33 original subtree **d01c92f7414713300934be3bb4e3d40ac57631b3** ve [RECONCILIATION](evidence/2026-09-11-multiturn/RECONCILIATION.md) korunur. Eski vaka sayıları bağımsız doğrulama/ürün puanı diye toplanmaz.

## Cold-start ve retrieval

1. Current main AGENT/tetiklenen protokoller→research root/studies catalog→META/STATE/INDEX→METHOD/PLAN. U14 PUBLICATION üstü actual yayın hükmüdür; A/B historical prepared ifadeleri tamamlanmış makbuzun yerine geçmez.
2. Note29 + A INSTALL-AND-ACTIVATION/INSTALL-SOURCES + B UPDATE-AND-RECOVERY/UPDATE-SOURCES + CHECKS-NOT-RUN tam okunur. U14 raw RESULT veya test arşivi yoktur. Opening/A/B tamamlanmış yayınları yeniden yapılacak iş sayma.
3. [Exact U13 STATE](https://github.com/batuhanozgun/agentic-os-search/blob/93d6b14438802163ed3f542beded218e14cc51cf/research/studies/hermes-agent/STATE.md) içindeki U13 A/B/SPEC/MANIFEST/NOT RUN/kapsam ve U12/U11/U10/synthesis/U04 mandatory ayrım yollarını izle. Exact eski D/N/C iddiası kendi tam RESULT/raw source/input/probe'una döner; sadece source devamında yeni test hükmü üretme.
4. Q59 başında [synthesis01](synthesis/01-LEARNING-AND-CHANGE-PROVISIONAL.md) ve onun eski approval/library residual yollarını karşı oku; completed çalışmayı yeniden araştırma sanma. Current library consumer'ları exact pin'den aç. Diğer üç synthesis kendi native alanlarında kalır, final CORE olmaz.
5. [U14 opening PLAN](https://github.com/batuhanozgun/agentic-os-search/blob/1d65fd3e701dcd7c3c84b7efebb99666ca9377e0/research/studies/hermes-agent/RESEARCH-PLAN.md), [A STATE](https://github.com/batuhanozgun/agentic-os-search/blob/c0d6418817e512137567e32c8d5aeabdb006f8f3/research/studies/hermes-agent/STATE.md), [B STATE](https://github.com/batuhanozgun/agentic-os-search/blob/2ce9310ad237bfaebcdbcc26ed5fc333f98b54ba/research/studies/hermes-agent/STATE.md) tarihsel kapılardır. Same-conversation değişmeyen full reads reuse olabilir, bağımsız evidence değildir. MAP/catalog derived, STATE veya raw yerine geçmez.
