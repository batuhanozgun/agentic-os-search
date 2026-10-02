#!/usr/bin/env python3
"""EXP-007 PreToolUse(Agent) kapısı: alt ajan görev metni STANDART.md'yi taşımıyorsa çağrıyı durdurur (DERSLER L2)."""
import json, sys
try:
    d = json.load(sys.stdin)
except Exception as e:
    print(f"ajan-standart-kapisi: girdi okunamadı ({e}); çağrı durduruldu, kapı bozuk olabilir.", file=sys.stderr)
    sys.exit(2)
if d.get("tool_name") != "Agent":
    sys.exit(0)
ti = d.get("tool_input") or {}
prompt = str(ti.get("prompt", ""))
if "STANDART.md" in prompt:
    sys.exit(0)
print("DURDURULDU (EXP-007 DERSLER L2): Alt ajan görev metni, "
      "/home/user/agentic-os-search/explorations/EXP-007-devos-claude-calisma-duzeni/devos/okuma/STANDART.md "
      "dosyasını zorunlu ilk okuma olarak içermeli. Görev metnine ekle ve yeniden çağır.", file=sys.stderr)
sys.exit(2)
