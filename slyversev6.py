
---

## FINANZAS – TRANSPARENCIA TOTAL

| Concepto               | Valor             |
|------------------------|-------------------|
| Precio Chalet          | {FINANZAS['chalet_price']:,.0f} €       |
| Gastos + ICO           | {FINANZAS['gastos']:,.0f} €         |
| **Total financiado**   | **{FINANZAS['total_ico']:,.0f} €**   |
| Cuota bruta (TIN 2.7%) | {FINANZAS['cuota_bruta']:,.2f} €/mes    |
| Deducción IRPF         | -{FINANZAS['deduccion_irpf']:,.2f} €         |
| **Cuota neta**         | **{FINANZAS['cuota_neta']:,.2f} €/mes**|
| **Ingresos éticos**    | **{FINANZAS['total_ingresos']:,} €/mes**   |
| **Cobertura ROI**      | **{FINANZAS['cobertura_roi']}%**        |
| **Excedente mensual**  | **+{FINANZAS['excedente_mensual']:,.2f} €**   |

> **La hipoteca se paga sola.**  
> **El excedente financia 22@.**

---

## INGRESOS ÉTICOS (MENSUALES)

```text
┌─ freelance_github → {FINANZAS['ingresos']['freelance_github']:,} €
├─ suite_colabs     → {FINANZAS['ingresos']['suite_colabs']:,} €
└─ minado_etico     → {FINANZAS['ingresos']['minado_etico']:,} €
══════════════════════════
TOTAL: {FINANZAS['total_ingresos']:,} € → 100% legal, 100% ético