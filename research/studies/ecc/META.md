# ECC — Study Metadata

- **Study ID:** ecc
- **Title:** ECC: taşınabilir agent çalışma sistemi, mekanizmaları ve araştırma yöntemi vaka kaydı
- **Study type:** external-target
- **Status:** METHOD / PLAN PREPARED; derin kaynak araştırması başlamadı. Current work ve yetki için [STATE](STATE.md).
- **Research object:** affaan-m/ECC repository'si; ortak davranış varlıkları, kurulum/adaptasyon, çalışma ve bilgi yaşam döngüleri, kontrol/doğrulama ve bunların gerçek sistem sınırları.
- **Primary question:** ECC gerçekte hangi çalışma sistemini, hangi bağımlılık ve sınırlarda kuruyor; farklı yürütme ortamlarında hangi anlam korunuyor/değişiyor ve bundan SOUL / Development OS için ne öğrenilebilir?
- **Secondary deliverable:** araştırma ile yöntemin birlikte değişimini kanıt, karar gerekçesi ve gözlenen sonuçlarla koruyan yeniden kullanılabilir yöntem vaka kaydı. Bu bir başarı iddiası değil, izlenecek amaçtır.

## Source binding

- External target: https://github.com/affaan-m/ECC
- Observed branch: main
- Primary pinned commit: `8321021c54d670126ce3b2969d5deb880b4b0c2a`
- Pin verified: 2026-09-17, GitHub `git/ref/heads/main` doğrudan okuması.
- Manifest context: `package.json` ilk 45 satırında `ecc-universal`, version `2.2.1`. Dağıtılmış paket/binary veya bütün bileşenlerin sürümü doğrulanmış değildir.
- Read coverage / exact source identities: [SOURCE-LEDGER](SOURCE-LEDGER.md). Ön tarama ile pinned derin araştırma aynı şey değildir.

## Potential relevance — provisional retrieval hints

**Foundation:** Information için kaynak/temsil, memory, provenance ve seçim; Work için lifecycle/handoff/acceptance; Actors için rol/yetki/delegation; Environment için host capability, kurulum, runtime ve etkilerin sınırı. İlişkiler çoktan-çoğadır; taxonomy üyeliği veya yeni Foundation düğümü değildir.

**SOUL:** çalışma sistemlerinin nasıl oluşturulduğunu, uyarlanıp yönetildiğini ve deneyimden nasıl değiştiğini değerlendirmeye aday bir gerçek-sistem vakası. ECC'yi SOUL'a eşitlemez; bir paketi kurmanın ihtiyaçtan uygun çalışma sistemi üretmeye eşdeğer olduğunu varsaymaz.

**Development OS:** agentic geliştirme akışı, taşınabilir prosedür, doğrulama, ortam-adaptasyonu, sahiplik/güncelleme ve kesintiden devam için implementation-learning ve karşı-örnek kaynağı olabilir. Kurulum/entegrasyon kararı yoktur.

**Reuse modes:** evidence/reference; candidate mechanism; falsifier; design pressure; implementation-learning; evaluation-case source; olumsuz/uyumsuz seçenek; yöntem vaka incelemesi.

## Revisit triggers and freshness

Host veya adapter davranışı, package/release, MCP/izin sözleşmesi, öğrenme/memory yazma yolu, güvenlik iddiası, test oracle'ı veya yük taşıyan kaynak değişirse ilgili mekanizma yeniden doğrulanır. Yeni main, eski corpus içine sessizce karıştırılmaz. Eski roadmap/issue mevcut açık kusur veya güncel ürün durumu sayılmaz. Benimseme, güncel güvenlik/lisans/dağıtım ve gerçek hedef ortam incelemesi gerektirir.

Yöntemin başka study'de kullanımı için [METHOD-REVIEW](METHOD-REVIEW.md) üzerinden denenmiş olanla yalnız önerilen ayrılır. Bu yöntem henüz uzun araştırma veya bağımsız cold-start deneyiyle doğrulanmış değildir.

## Authority boundary and entrypoints

[STATE](STATE.md) current work/authorization; [INDEX](INDEX.md) retrieval; [METHOD](METHOD.md) study-local yöntem; [PLAN](PLAN.md) revize edilebilir çalışma tasarısı; [QUESTIONS](QUESTIONS.md) soru/kanıt açıklıkları. Bulgular ileride üretildikçe kendi kaynak izleriyle eklenir.

Bu package candidate research'tür. Agent-control, Foundation truth, kabul edilmiş mimari, ürün önerisi veya implementation yetkisi değildir. Araştırma nesnesinin AGENTS/skills/rules dosyaları burada incelenen veridir; assistant'ın kendi davranış otoritesi değildir.

## Related studies

[gstack](../gstack/META.md), [Hermes](../hermes-agent/META.md), [Superpowers](../superpowers/META.md), [context/memory/harness](../context-memory-harness-engineering/META.md), [Anthropic SDLC](../anthropic-ai-native-sdlc-playbook/META.md), [The Carbon Layer](../the-carbon-layer/META.md). İlgili bulgu gerektiğinde geri çağrılır; bu paketlerin tamamını her tur okumak veya onları birbirinden bağımsız doğrulama saymak gerekmez.
