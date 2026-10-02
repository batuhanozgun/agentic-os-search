#!/usr/bin/env python3
"""Claude Code oturumunun gerçek token kullanımını transcript'lerden ölçer.

Neden var: Görev bildirimlerindeki `subagent_tokens` alanı bir ajanın toplam
harcamasını göstermiyor (27 Eylül 2026'da T4 için bildirim 77,9 K derken
transcript 20,8 M işlenen token gösterdi). Bu betik her API çağrısının
`usage` alanını, mesaj kimliğine göre tekilleştirerek toplar.

Kullanım:
    python3 token-kullanimi.py [transcript.jsonl veya klasör ...]
Argüman verilmezse ~/.claude/projects altındaki bütün transcript'ler okunur.
Bir oturumun alt ajan ve workflow transcript'leri
~/.claude/projects/<proje>/<oturum-kimliği>/subagents/ altındadır.

Sınırlar:
- Çıktı token'ları eksik sayılıyor olabilir: akış sırasında yazılan kayıtlar
  mesajın son kullanım değerini taşımayabilir. Girdi ve önbellek sayıları
  güvenilirdir.
- "Girdi eşdeğeri", API fiyat oranlarıyla yapılan kaba bir ağırlıktır:
  önbellekten okuma 0,1x, önbelleğe yazma 1,25x (5 dk) ya da 2x (1 saat),
  çıktı 5x. Abonelik limitlerinin bunları nasıl saydığı bilinmiyor.
- Makine geri alınınca transcript'ler kaybolur; ölçüm oturum içinde yapılıp
  sonucu kayda (STATE) yazılmalıdır.
"""
import glob
import json
import os
import sys


def dosyalar(argumanlar):
    if not argumanlar:
        argumanlar = [os.path.expanduser("~/.claude/projects")]
    for a in argumanlar:
        if os.path.isdir(a):
            yield from sorted(glob.glob(os.path.join(a, "**", "*.jsonl"), recursive=True))
        else:
            yield a


def kullanim(yol):
    gorulen = {}
    with open(os.path.realpath(yol), encoding="utf-8", errors="replace") as f:
        for satir in f:
            try:
                d = json.loads(satir)
            except ValueError:
                continue
            m = d.get("message")
            if d.get("type") != "assistant" or not isinstance(m, dict):
                continue
            if m.get("usage") and m.get("id"):
                gorulen[m["id"]] = m["usage"]
    t = lambda k: sum(u.get(k, 0) for u in gorulen.values())
    tepe = max((u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
                + u.get("cache_read_input_tokens", 0)) for u in gorulen.values()) if gorulen else 0
    return {"cagri": len(gorulen), "girdi": t("input_tokens"),
            "onbellege_yazma": t("cache_creation_input_tokens"),
            "onbellekten_okuma": t("cache_read_input_tokens"),
            "cikti": t("output_tokens"), "tepe_baglam": tepe}


def m(n):
    return f"{n / 1e6:.1f}M"


def main():
    toplam = dict.fromkeys(["cagri", "girdi", "onbellege_yazma", "onbellekten_okuma", "cikti"], 0)
    for yol in dosyalar(sys.argv[1:]):
        k = kullanim(yol)
        if not k["cagri"]:
            continue
        for a in toplam:
            toplam[a] += k[a]
        islenen = k["girdi"] + k["onbellege_yazma"] + k["onbellekten_okuma"] + k["cikti"]
        print(f"{os.path.relpath(yol)}: çağrı={k['cagri']} işlenen={m(islenen)} "
              f"önbellekten_okuma={m(k['onbellekten_okuma'])} tepe_bağlam={k['tepe_baglam']:,}")
    islenen = toplam["girdi"] + toplam["onbellege_yazma"] + toplam["onbellekten_okuma"] + toplam["cikti"]
    esdeger = lambda yazma: (toplam["girdi"] + toplam["onbellege_yazma"] * yazma
                             + toplam["onbellekten_okuma"] * 0.1 + toplam["cikti"] * 5)
    print(f"TOPLAM: çağrı={toplam['cagri']} işlenen={m(islenen)} "
          f"(önbellekten okuma {m(toplam['onbellekten_okuma'])}, önbelleğe yazma {m(toplam['onbellege_yazma'])}, "
          f"çıktı {m(toplam['cikti'])}); girdi eşdeğeri ≈ {m(esdeger(1.25))}–{m(esdeger(2))}")


if __name__ == "__main__":
    main()
