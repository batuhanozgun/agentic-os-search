# keel — okuma defteri

Repo: `batuhanozgun/keel`  
Rol: somutlaşmış ürün/mekanizma yüzeyi  
Okuma stratejisi: öz-anlatı → kurucu model → defo modeli → seçici mekanik doğrulama

## Neden önemli

KEEL, durumsuz ajanlarla yazılım projesi kurup yürütmek için geliştirilmiş bir işletim disiplini. SOUL'un doğrudan öncülü olduğu varsayılmıyor; fakat oturum sürekliliği, rol/motivasyon ayrımı, insan karar kapıları, mekanik iz ve doğrulama gibi problemler üzerinde somut tasarım deneyimi taşıyor.

SOUL genel amaçlı bir agentic architecture hedeflediği için, KEEL'deki her mekanizma iki soruyla okunacak:

1. Hangi gerçek problem/failure mode'u çözmeye çalışıyor?
2. Bu çözüm yazılım-projesi/Claude Code bağlamına mı özgü, yoksa daha genel bir ilke mi taşıyor?

## Okuma kaydı

| Kaynak | SHA | Tür | Neden | Maddi bulgu / işaretçi |
|---|---|---|---|---|
| kök içerik ağacı | — | index | giriş yüzeyini bulmak | `README.md`, `GENESIS.md`, `00_genesis/`, `.claude/`, `docs/`, `tools/` ana yüzeyler |
| `README.md` | `a221d174` | full | ürünün açık amacı ve kullanım modeli | KEEL, dağınıklık/unutkanlık sorununa kanon, roller, kutular, mühürler ve kokpit ile cevap veren kurulum sistemi; "bilerek az anla, çalışan sistem bırak" ilkesi merkezi |
| `GENESIS.md` | `a04b8060` | full | kurucu akışın sınırlarını anlamak | product plan yapmayan tek-seferlik kurucu; sabit plan, mühürler, çıkış ölçütleri, state dosyası ve mekanik sıra ile yarım oturum güvenliği |
| `00_genesis/DEFO_MODELI.md` | `e9bddf5e` | full | mekanizmaların varsayılan ajan modeli | on defo: yağcılık, aynalama, şişme, drift, sahte-menü, uydurma, öz-onaylama, donma/aşırı-sorma, karar-yükleme, örtme; yumuşak öz-yargı yerine gözlemlenebilir iz/mekanik kapı tercih ediliyor |

## İlk tematik çıkarımlar — SONUÇ DEĞİL

- KEEL, ajan davranışını yalnız prompt talimatıyla düzeltmeye güvenmiyor; mümkün olduğunda state, guard, fixture, test ve insan mührü gibi dışsal yapılara çeviriyor.
- "Durumsuz-güvenlik" ve canonical state fikri SOUL'un development OS ayrımıyla ilişkili olabilir; ancak bunu genellemeden önce os-architect kök nedenleri okunmalı.
- Def o modelindeki kök itki güçlü bir açıklama iddiası. Bu iddia doğrudan SOUL gereksinimi kabul edilmeyecek; kaynak araştırması ve karşı-kanıt aranacak.

## Sonraki okuma — şimdilik beklemede

Önce `os-architect` içindeki kök neden ve araştırma kayıtları okunacak. Ardından KEEL mekanikleri seçici olarak sınanacak.

Muhtemel hedef yüzeyler:

- `00_genesis/adimlar/` — state ve kapıların yaşam döngüsü,
- `tools/guard/` — yazma/kurulum koruması,
- `tools/bekci/` — sağlık/denetim mekanikleri,
- `tools/kokpit/test/fixtures/` — format ve parser oracle'ları,
- `.claude/` — rol/izin/hook yüzeyleri,
- `docs/` — sözleşme ve kavram tanımları.

Bu klasörler toplu okunmayacak; os-architect'teki bir iddia veya açık soru hangi mekanizmaya işaret ediyorsa o dosya açılacak.

## Açık sorular

- Def o modelinin her maddesi hangi somut gözlem/deneyden türedi?
- Hangi mekanizmalar yanlış durumda gerçekten kırmızı verebiliyor?
- Hangi kontroller yalnız Claude Code hook/runtime özelliklerine bağımlı?
- İnsan mühürleri hangi karar sınıflarında epistemik güvence, hangilerinde yalnız yetki sınırı?
- State/kanon/role yapısının hangi parçaları genel amaçlı agentic architecture'a taşınabilir?
- KEEL'in kendi testleri sistemin iddia ettiği davranış sınıflarını gerçekten ölçüyor mu?
