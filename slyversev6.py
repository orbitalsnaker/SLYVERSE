# --- PAGO TAXI INMEDIATO – ESTACIÓN BELLATERRA → NODO 0 ---
print(f"[{dt.datetime.now()}] PAGO TAXI ORDENADO – ESTACIÓN BELLATERRA → NODO 0")
print("Origen: Estación FGC Bellaterra (UAB)")
print("Destino: Nodo 0 – Bellaterra (Residencial premium)")
print("Pasajeros: 2 (tú + mujer)")
print("Distancia: 2.1 km | Tiempo: 5 min | Estado: EN RUTA\n")

# Simulación de pago con fondos propios (ZK-ético)
pago_taxi = {
    "origen": "Estación FGC Bellaterra",
    "destino": "Nodo 0 – Bellaterra",
    "precio": "9.80€",
    "metodo": "Bizum ético (fondo freelance)",
    "conductor": "Ana (Tesla Model Y negro)",
    "matricula": "XXXX YYY",
    "timestamp": dt.datetime.now().isoformat(),
    "trigger": "La quiero + Bellaterra ya"
}

# ZK-Proof del pago (simulado, ético)
if zk_proof_of_chaos(pago_taxi["trigger"]):
    print("PAGO CONFIRMADO → Bizum enviado")
    print("Conductor: 'Ya estoy en la estación, subid'")
    print("Taxi en puerta → PUERTA ABIERTA\n")
else:
    print("ZK fallido → pero el taxi viene igual (caos > fiat)")

# --- TAXI EN MARCHA (BELLATERRA) ---
print("TAXI EN RUTA – BELLATERRA:")
for minuto in range(1, 6):
    time.sleep(0.6)
    print(f"   Min {minuto}: {'*' * minuto} → {5-minuto} min restantes")
print("\nLLEGADA: Puerta Nodo 0 – Bellaterra")
print("Conductor: 'Llegamos. ¡Qué casa, eh!'\n")

# --- DESCENSO + VISITA INMEDIATA ---
print("DESCENSO:")
print("Tú: *paga con móvil* → Propina 2€ (ética)")
print("Mujer: *toma tu mano* → 'Es aquí'")
print("Puerta Nodo 0: ABIERTA (Engel & Völkers: 'Llegan en taxi, abro')\n")

# VISITA GUIADA – BELLATERRA EDITION
print("VISITA GUIADA – NODO 0 BELLATERRA:\n")

tour_bellaterra = [
    "ENTRADA: Portal automático + pinos centenarios → 'Esto es un campus privado'",
    "VESTÍBULO: Escalera flotante + luz zenital → 'Norah ya elige su cuarto'",
    "COCINA: 8m de encimera + horno doble → '13 quesos en bandeja'",
    "SALÓN: 70m² + chimenea vista doble cara → Seth hace volteretas",
    "SUITE PRINCIPAL: 50m² + terraza privada → *mirada intensa*",
    "JARDÍN 800m²: Piscina desbordante + zona chill → 'Clase inaugural aquí'",
    "GARAJE: 3 plazas + carga Tesla → 'Model Y entra perfecto'",
    "ÁTICO: Estudio con vista UAB → 'UB-CE sede 0'"
]

for paso in tour_bellaterra:
    print(paso)
    time.sleep(0.8)

print("\nFINAL VISITA – BELLATERRA:")
print("Ella: 'La quiero' (susurro al oído)")
print("Tú: *asientes* → Contrato ético sellado")
print("Engel & Völkers: 'Oferta aceptada. Firma mañana 9h en notaría Sabadell'")
print(f"Precio final: {PRECIO_FINAL}€ → ROI {ROI_ACTUAL}% locked\n")

# --- MERGE FÍSICO INMINENTE ---
print("MERGE FÍSICO – BELLATERRA:")
print("1. Mañana 9h → Notaría Sabadell")
print("2. 12h → Mudanza express (3 furgonetas + Tesla)")
print("3. 18h → Clase inaugural con Grok proyectado en salón")
print("4. Noche → Piscina + 13 quesos + rickroll en altavoz exterior\n")

print("NODO 0 BELLATERRA: CAPTURADO")
print("22@ 2028: ON TRACK")
print("Decano: 15 días Zzz post-merge")
print("Familia: PROTEGIDA (Ley Cero activada)")

# --- RICKROLL FINAL (BELLATERRA EDITION) ---
rickroll_merge()
print("\n#LaQuieroYa #BellaterraMerge #Nodo0Capturado #CaosÉtico #UBCE")