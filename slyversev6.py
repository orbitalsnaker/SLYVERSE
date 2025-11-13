#!/usr/bin/env python3
# SLYVERSE_UNIVERSITY_v6.1_URGENT.py
# Decano: @0rb1t4lsn4k3r
# Director: @grok (xAI)
# Fecha: 13 NOV 2025 – 18:15 CET
# OBJETIVO: CASA EN BELLATERRA EN 30 DÍAS
# Estrategia: Excedente + P2P + PRs + Ko-fi → 50.000€ en 4 semanas

import time
import webbrowser
import json
from datetime import datetime, timedelta

# =============================================
# CONFIGURACIÓN URGENTE — CASA YA
# =============================================
DECANO = "@0rb1t4lsn4k3r"
DIRECTOR = "@grok"
CASA_OBJETIVO = 50000  # € para entrada + fianza + mudanza
DIAS_MAX = 30
HOY = datetime.now()
FECHA_LIMITE = HOY + timedelta(days=DIAS_MAX)

# INGRESOS REALES (edita si cambia)
INGRESOS_MENSUAL = 8500
EXCEDENTE_MENSUAL = 1520.14
DIAS_PARA_CASA = min(DIAS_MAX, 30)

# ACELERADORES URGENTES
ACELERADORES = {
    "p2p_diario": 500,      # Venta diaria $SLY → Bizum
    "pr_github": 1000,      # 1 PR aceptado = 1.000€
    "ko_fi_donacion": 300,  # Meta diaria apoyo
    "freelance_extra": 2000 # 1 cliente nuevo
}

# =============================================
# CÁLCULO URGENTE
# =============================================
def calcular_casa_ya():
    total_acelerado = sum(ACELERADORES.values()) * DIAS_PARA_CASA
    total_excedente = EXCEDENTE_MENSUAL * (DIAS_PARA_CASA / 30)
    total_proyectado = total_acelerado + total_excedente
    faltan = max(0, CASA_OBJETIVO - total_proyectado)
    
    print(f"\n{'='*70}")
    print(f" SLYVERSE v6.1 URGENT — CASA EN {DIAS_MAX} DÍAS")
    print(f"{'='*70}")
    print(f" Decano: {DECANO} | Director: {DIRECTOR}")
    print(f" Fecha límite: {FECHA_LIMITE.strftime('%d/%m/%Y')}")
    print(f" Objetivo: {CASA_OBJETIVO:,}€")
    print(f"{'='*70}")
    print(f" ACELERADORES DIARIOS:")
    for k, v in ACELERADORES.items():
        print(f"   • {k.replace('_', ' ').title()}: +{v:,}€")
    print(f"{'-'*70}")
    print(f" Proyectado en {DIAS_PARA_CASA} días: {total_proyectado:,.0f}€")
    print(f" Excedente base: +{total_excedente:,.0f}€")
    print(f" FALTAN: {faltan:,.0f}€ → CUBRIMOS CON PRs + KO-FI")
    print(f"{'='*70}\n")
    return total_proyectado, faltan

# =============================================
# ACCIONES URGENTES
# =============================================
def accion_urgente():
    print("[ACCIONES] EJECUTA HOY:")
    print("   [1] → Vender $SLY (P2P Bizum → 500€)")
    print("   [2] → Subir PR (GitHub → 1.000€)")
    print("   [3] → Post Ko-fi (Apoyo → 300€)")
    print("   [4] → Buscar cliente (Freelance → 2.000€)")
    print("   [5] → Idealista Bellaterra (Buscar casa)")
    print("   [S] → Salir")

def ejecutar(accion: str):
    if accion == "1":
        print("Abriendo Binance P2P → vende 500€ en USDT")
        webbrowser.open("https://p2p.binance.com")
    elif accion == "2":
        print("Abriendo GitHub → sube PR ético")
        webbrowser.open("https://github.com/orbitalsnaker/SLYVERSE/pulls")
    elif accion == "3":
        msg = f"URGENTE: Necesito casa en Bellaterra. Apoya SLYVERSE → {CASA_OBJETIVO}€ en {DIAS_MAX} días #LaQuiero"
        url = f"https://x.com/intent/post?text={msg}"
        print("Posteando en X → Ko-fi")
        webbrowser.open(url)
        webbrowser.open("https://ko-fi.com/slyverse")
    elif accion == "4":
        print("Buscando cliente freelance → Upwork/Fiverr")
        webbrowser.open("https://www.upwork.com/freelancers/~01...")
        webbrowser.open("https://www.fiverr.com")
    elif accion == "5":
        print("Buscando casa en Bellaterra → Idealista")
        webbrowser.open("https://www.idealista.com/buscar-alquiler-viviendas/bellaterra/")
    elif accion == "S":
        return False
    return True

# =============================================
# PROGRESO EN TIEMPO REAL
# =============================================
def guardar_progreso(proyectado: float, faltan: float):
    progreso = {
        "fecha": HOY.isoformat(),
        "objetivo": CASA_OBJETIVO,
        "proyectado": round(proyectado),
        "faltan": round(faltan),
        "acciones_pendientes": list(ACELERADORES.keys()),
        "fecha_limite": FECHA_LIMITE.isoformat()
    }
    with open("casa_ya_progress.json", "w") as f:
        json.dump(progreso, f, indent=2)
    print(f"[PROGRESO] Guardado en casa_ya_progress.json")

# =============================================
# MAIN — v6.1 URGENT
# =============================================
def main():
    proyectado, faltan = calcular_casa_ya()
    accion_urgente()
    guardar_progreso(proyectado, faltan)
    
    while True:
        accion = input("\nEjecuta HOY (1/2/3/4/5/S): ").strip()
        if not ejecutar(accion):
            break
        time.sleep(1)
    
    print("\n" + "="*70)
    print(" SLYVERSE v6.1 URGENT — CASA EN MARCHA")
    print(f" Decano: {DECANO} | Director: {DIRECTOR}")
    print(f" Faltan {faltan:,.0f}€ → TÚ LOS CONSEGUIRÁS")
    print(" Mañana repetimos. Hasta tener la casa.")
    print(" #LaQuiero #CasaYa #v6.1 #Real")
    print("="*70)

if __name__ == "__main__":
    main()