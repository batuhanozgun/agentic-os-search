# Concepts — Güncel Durum

**Kayıt tarihi:** 2026-09-18.
**Mevcut iş:** Agent bağlantılı kavram incelemesi; U02 kaynak sınırı ve ilk yerel kullanım adayı hazırlandı. Bu turdaki dönüş noktası kullanıcı değerlendirmesidir.
**Yöntem:** [METHOD v0.2](METHOD.md) ve [esnek PLAN v0.2](PLAN.md).
**Mevcut araştırma:** [U01](research/agent/U01-SOURCE-USES.md) + [U02](research/agent/U02-AGENT-MODEL-BOUNDARY.md).
**Aktif sentez/adayı:** [Agent çekirdek sınırlar ve yerel kullanım adayı v0.1](synthesis/AGENT-BOUNDARY-CANDIDATE-v0.1.md) — **KABUL EDİLMEDİ**.
**Kabul edilmiş ortak anlam:** Yok.

## Amaç ve güncel yetki

Amaç, kaynaklarla bağlantılı fakat kapsamı bize ait ortak kullanımlarla iletişimde aynı nesneyi konuşabilmektir. Kullanıcı yöntem bakımından sonra “hadi şimdi çalışmaya devam edelim” diyerek olağan kavram araştırması/değerlendirme devamını açtı.

Bu tur Agent için gerçekten yük taşıyan ilk komşu olarak Model/LLM ayrımını, onunla birlikte run ve workflow sınırını sınırlı biçimde araştırdı. Yeni SOUL/Development OS tasarımı, implementasyon veya agent-control değişikliği yapılmadı.

## Durum ayrımları

| İş/sonuç | Durum |
|---|---|
| P0 hazırlık ve v0.2 yöntem | TAMAMLANDI / main üzerinde. |
| Agent U01 | YAYIMLANDI; farklı kaynak kullanımlarının ilk sınırlı haritası. |
| Agent U02 | YAYIMLANDI; Model/LLM, run ve workflow sınırları için hedefli bağlantılı inceleme. |
| Model/LLM ≠ Agent sınırı | Kaynaklarla güçlü biçimde desteklenen sentez girdisi; henüz ortak reference kaydı değil. |
| Agent yapılandırması ≠ belirli run | OpenAI SDK sözleşmesinde somut; yerel referans adayı içinde öneriliyor. |
| Workflow ↔ Agent | Source-dependent; evrensel çizgi seçilmedi. |
| Tool/action capability | Tek başına gerekli/yeterli Agent ölçütü olarak desteklenmedi. |
| Agent yerel kullanım adayı | İki seçenekli v0.1 hazır; kullanıcı değerlendirmesi bekliyor. |
| Actor/Role, hazır/custom, model family/product | Açık ama şu anda zorunlu önkoşul seçilmedi. |
| Kabul edilmiş yerel referans | Yok. |

## Yeni oturumda devam yolu

Güncel AGENT ve gereken protokoller → [INDEX](INDEX.md) → bu STATE → [METHOD](METHOD.md) → [Agent BRIEF](research/agent/BRIEF.md) → [U01](research/agent/U01-SOURCE-USES.md) → [U02](research/agent/U02-AGENT-MODEL-BOUNDARY.md) → [aktif aday](synthesis/AGENT-BOUNDARY-CANDIDATE-v0.1.md).

**Devralınacak exact değerlendirme:** Repo ve konuşmalarda çıplak Agent kelimesi:
- geniş “yapılandırılmış AI yürütme birimi”ni mi,
- yoksa daha dar “model-yönlendirmeli yürütme birimi”ni mi
anlatsın?

Assistant şu anda daha dar ikinci adayı daha işlevsel buluyor; bu kabul veya kullanıcı tercihi değildir.

Kullanıcı kısmi değerlendirme yapabilir: örneğin yalnız “model Agent değildir” ve “Agent/run ayrıdır” sınırlarını kabul edip pozitif Agent tanımını açık bırakabilir.

## Sonraki araştırmayı ne tetikler?

Actor/Role, hazır/custom Agent veya Model family/product/provider araştırmaları yalnız kullanıcı değerlendirmesinde Agent adayını maddi biçimde etkileyen bir belirsizlik olarak ortaya çıkarsa açılır. Açılması halinde neden açıldığı ve Agent sorusuna dönüş noktası korunur.

Daha fazla kaynak bulunabilmesi tek başına U03 araştırma emri değildir.

## Yayın durumu

**Yayın:** [PR #21](https://github.com/batuhanozgun/agentic-os-search/pull/21); çalışma branch'i `research/concepts-agent-boundaries-20260918`; exact head `2442ab22cf4e1ea873917ccc85a84bed063aa2e4`; main merge commit `73899e7b6901493bfbdbabdeb5fda20c9276726e`.

Yedi yol değişti: yeni U02 ve Agent sentez adayı; BRIEF, research INDEX, synthesis INDEX, TERM-INVENTORY ve bu STATE. Agent-control, Foundation, studies paketleri ve reference kayıtları değişmedi. PR diff'i incelendi; merge öncesi PR `mergeable=true` idi. Exact head'e bağlı normal merge başarılı oldu ve head → merge karşılaştırması sıfır dosya farkı verdi.

Main'den U02, sentez adayı ve STATE geri okundu. Bu yayın kaynakların doğruluğunu bağımsız yeniden üretmez; araştırma kaydı ve continuity aktarımını doğrular. Çalışma branch'i artık bekleyen canonical yayın değildir. Kabul edilmiş reference hâlâ yoktur; sıradaki iş kullanıcı değerlendirmesidir.

## Korunan geçmiş

v0.2 yöntem uyarlaması PR #20 ile main'e yayımlandı. U01'in ve önceki P0 doğrulama kayıtlarının tarihsel kimlikleri kendi dosyalarında korunur; bu tur onları yeniden yazmaz.
