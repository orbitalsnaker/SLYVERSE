#!/usr/bin/env python3
# SLYVERSE_ROI_REAL_v1.0.py
# Autor: @0rb1t4lsn4k3r (Decano)
# Sin Grok. Sin universidad. Solo ROI real.
# Ejecuta en cualquier PC/móvil con Python.
# Genera €1.520+/mes → 22@ financiado.

import time
import webbrowser
from datetime import datetime

# === TUS INGRESOS REALES (edita esto) ===
INGRESOS = {
    "freelance_github": 2800,
    "suite_colabs": 1500,
    "minado_sly": 4200
}
TOTAL_INGRESOS = sum(INGRESOS.values())

# === GASTOS REALES (edita esto) ===
CUOTA_HIPOTECA = 6979.86  # neta
EXCEDENTE = TOTAL_INGRESOS - CUOTA_HIPOTECA

# === ROI REAL ===
ROI = (TOTAL_INGRESOS / CUOTA_HIPOTECA) * 100

# === PLAN 22@ (5 años) ===
MESES = 60
FONDO_5ANOS = EXCEDENTE * MESES
SUBVENCION_UE = 2000000
TOTAL_22 = FONDO_5ANOS + SUBVENCION_UE

# === ACCIONES REALES (sin mí) ===
def abrir_p2p():
    print("[