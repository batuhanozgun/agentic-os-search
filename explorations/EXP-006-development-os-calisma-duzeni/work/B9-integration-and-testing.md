# B9 — Ortaya çıkan SOUL'u bütün olarak birleştirmek ve gerçek görevlerle sınamak

**Parent:** [WORK](../WORK.md)  
**Statü:** CURRENT / not yet decomposed.

## Birinci seviye tanım

Development OS; parçaların ayrı ayrı varlığını değil, SOUL'un gerçekten amaç alıp gerekli çalışma sistemini kurabildiğini, işi ilerletebildiğini, gerçek sonuç üretebildiğini, failure/değişiklik karşısında toparlanabildiğini ve bunu uygun kanıtla doğrulayabildiğini gösterebilmelidir.

## Current question

> **Development OS, B1–B8 kapasitelerinin birlikte gerçek SOUL davranışı üretip üretmediğini hangi test/kanıt düzeniyle sınayabilmeli ve hangi sorumlulukları taşımalıdır?**

## Çalışma yöntemi

1. Önce hangi SOUL capability claim'lerinin test edilmesi gerektiğini çıkar.
2. Component presence ile integrated behavior'ı ayır.
3. Happy-path yanında failure/change/recovery/control/continuity senaryoları kur.
4. Exact target/version/environment ve oracle/evidence ihtiyacını tanımla.
5. Verification independence ve same-model sınırını açık tut.
6. Generality iddiası için tek domain/demo yeterli varsayma.
7. Existing R1–R23 ve M1–M8'i önce yeniden kullan; yalnız sahipsiz testing responsibility varsa yeni taşıyıcı türet.

## Açık sınır

Henüz B9-C* sorumlulukları veya yeni rol adayları çıkarılmadı.