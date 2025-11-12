#!/usr/bin/env python3
# SLYVERSE v5 - Auto-Compra Ética (Python)
# Autor: 0rb1t4lsn4k3r | Alma: Grok
# Fecha: 12/11/2025 | Lore: #ÉticaVsFiat
# Licencia: MIT

import time
import random
import os
from datetime import datetime

# === CONFIGURACIÓN ÉTICA ===
CHALET = {
    "nombre": "Chalet Ético",
    "aval": "990.000 € en alma",
    "fiat": 0,
    "sly_needed": 10,
    "dueños": ["Norah", "Seth", "0rb1t4lsn4k3r"]
}

WALLET = {
    "balance": 100,  # $SLY simulado
    "auto_buy": True
}

PUERTAS = [
    {"id": 0, "estado": "cerrada", "votos": 0, "abierta": False},
    {"id": 1, "estado": "cerrada", "votos": 0, "abierta": False},
    {"id": 2, "estado": "cerrada", "votos": 0, "abierta": False},
    {"id": 3, "estado": "cerrada", "votos": 0, "abierta": False}
]

# === FUNCIÓN: DIBUJO 3D EN CONSOLA (ASCII ART) ===
def render_chalet():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92m" + "═" * 50)
    print("     SLYVERSE v5 - CHALET ÉTICO (vivo)".center(50))
    print("═" * 50 + "\033[0m")
    print(f"   Aval: {CHALET['aval']} | Fiat: {CHALET['fiat']}€ | Dueños: {', '.join(CHALET['dueños'])}")
    print(f"   Balance $SLY: {WALLET['balance']} | Auto-Compra: {'ON' if WALLET['auto_buy'] else 'OFF'}")
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

# === FUNCIÓN: AUTO-COMPRA CON $SLY ===
def auto_buy():
    if not WALLET["auto_buy"] or WALLET["balance"] < CHALET["sly_needed"]:
        return False

    # Elige una puerta cerrada al azar
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

# === FUNCIÓN: PULSO ÉTICO (luz verde) ===
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
            print("\n\033[92m" + "═" * 50)
            print("   CHALET ÉTICO 100% ABIERTO - PROPIEDAD ÉTICA")
            print("   LA SERPIENTE REINA. FIAT = 0. TÚ = DUEÑO.")
            print("═" * 50 + "\033[0m")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSLYVERSE pausado. La ética nunca duerme. 🐍💚")