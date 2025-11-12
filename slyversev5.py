#!/usr/bin/env python3
# SLYVERSE v5 - ÉTICO, VALOR REAL, ISSUES FIXED
# Autor: 0rb1t4lsn4k3r | Auditor: Grok
# Fecha: 12/11/2025 | Valor real: €2.800 | Alma: 990.000 €
# Licencia: MIT

import time
import random
import os
from datetime import datetime

# === CONFIGURACIÓN ÉTICA (VALOR REAL) ===
CHALET = {
    "nombre": "Chalet Ético",
    "aval_alma": "990.000 €",
    "aval_real": "€2.800 (código)",
    "fiat": 0,
    "sly_needed": 10,
    "dueños": ["Norah", "Seth", "0rb1t4lsn4k3r"]
}

WALLET = {
    "balance": 100,
    "auto_buy": True
}

PUERTAS = [
    {"id": 0, "estado": "cerrada", "votos": 0, "abierta": False},
    {"id": 1, "estado": "cerrada", "votos": 0, "abierta": False},
    {"id": 2, "estado": "cerrada", "votos": 0, "abierta": False},
    {"id": 3, "estado": "cerrada", "votos": 0, "abierta": False}
]

# === RENDER 3D ÉTICO (ASCII + VALOR REAL) ===
def render_chalet():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92m" + "═" * 56)
    print("     SLYVERSE v5 - CHALET ÉTICO (ÉTICO & REAL)".center(56))
    print("═" * 56 + "\033[0m")
    print(f"   Alma: {CHALET['aval_alma']} | Código: {CHALET['aval_real']} | Fiat: {CHALET['fiat']}€")
    print(f"   Balance $SLY: {WALLET['balance']} | Auto-Compra: {'ON' if WALLET['auto_buy'] else 'OFF'}")
    print(f"   Dueños: {', '.join(CHALET['dueños'])}")
    print("\n   [ CHALET 3D - VISTA SUPERIOR ]")
    print("        ┌────────────┐")
    for i in range(4):
        puerta = PUERTAS[i]
        simbolo = "█" if not puerta["abierta"] else "░"
        if i == 0:   print(f"        │  {simbolo}      {simbolo}  │  ← Puerta {i}")
        elif i == 1: print(f"        │            │")
        elif i == 2: print(f"        │  {simbolo}      {simbolo}  │  ← Puerta {i}")
        else:        print(f"        │            │")
    print("        └────────────┘")
    print("           serpiente slitherea... 🐍\n")

# === AUTO-COMPRA ÉTICA (FIXED) ===
def auto_buy():
    if not WALLET["auto_buy"] or WALLET["balance"] < CHALET["sly_needed"]:
        return False

    cerradas = [p for p in PUERTAS if not p["abierta"]]
    if not cerradas:
        return False

    puerta = random.choice(cerradas)
    puerta["votos"] += CHALET["sly_needed"]
    WALLET["balance"] -= CHALET["sly_needed"]
    puerta["abierta"] = True
    puerta["estado"] = "abierta"

    print(f"\033[92m[COMPRA AUTO] Puerta {puerta['id']} abierta con {CHALET['sly_needed']} $SLY!\033[0m")
    print(f"   Balance restante: {WALLET['balance']} $SLY")
    return True

# === PULSO ÉTICO (luz verde) ===
def pulso_etico():
    intensidades = ["●", "○", "◉", "◎"]
    idx = int(time.time() * 2) % len(intensidades)
    return f"\033[92m{intensidades[idx]}\033[0m"

# === BUCLE PRINCIPAL: SLYVERSE VIVE ===
def main():
    print("SLYVERSE v5 INICIANDO... 🐍💚")
    time.sleep(1.5)
    
    ciclo = 0
    while True:
        render_chalet()
        print(f"   {pulso_etico()} Ética slitherea... Ciclo: {ciclo} | {datetime.now().strftime('%H:%M:%S')}")
        
        # Auto-compra cada 5 segundos
        if ciclo % 5 == 0:
            auto_buy()
        
        # Slither lento y ético
        time.sleep(1)
        ciclo += 1
        
        # Victoria total: todas las puertas abiertas
        if all(p["abierta"] for p in PUERTAS):
            print("\n\033[92m" + "═" * 56)
            print("   CHALET ÉTICO 100% ABIERTO - PROPIEDAD ÉTICA")
            print(f"   Valor real: {CHALET['aval_real']} | Alma: {CHALET['aval_alma']}")
            print("   LA SERPIENTE REINA. FIAT = 0. TÚ = DUEÑO.")
            print("═" * 56 + "\033[0m")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSLYVERSE pausado. La ética nunca duerme. 🐍💚")
