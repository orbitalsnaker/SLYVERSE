# SLYVERSE v1 — FINAL EDITION

**Single HTML file | 100% standalone | Forged in silence, polished in entropy.**

[![GitHub last commit](https://img.shields.io/github/last-commit/orbitalsnaker/SLYVERSE)](https://github.com/orbitalsnaker/SLYVERSE/commits/main)
[![PWA Ready](https://img.shields.io/badge/PWA-Ready-green)](https://web.dev/progressive-web-apps/)
[![WebXR](https://img.shields.io/badge/WebXR-Ready-blue)](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API)
[![WCAG AA](https://img.shields.io/badge/WCAG-AA-green)](https://www.w3.org/WAI/standards-guidelines/wcag/)

## 🎮 Live Demo
[Play SLYVERSE](https://raw.githubusercontent.com/orbitalsnaker/SLYVERSE/main/slyverse.html)  
*(Right-click → Save As → Open in browser. Works offline.)*

## ¿Qué es SLYVERSE?
Snake reimaginado en WebXR con grid toroidal (wrap-around), leaderboard global, power-ups raros, controles móviles nativos, PWA instalable y mock-miner de "$SLY" (queso).  
**v1 FINAL**: Todo en un archivo HTML5 <20KB. Sin dependencias externas.

## 🚀 Características Técnicas

| Feature | Descripción |
|---------|-------------|
| **Single-file** | 100% standalone HTML/JS/CSS. Copia-pega y juega. |
| **Responsive** | PC/móvil/tablet. Swipe + botones táctiles. |
| **PWA** | Instalable como app (manifest inline). |
| **Leaderboard** | Local (localStorage). Top 10 persistente. |
| **Wrap-around** | Portal-style: sale por un lado, entra por opuesto. |
| **Visuals** | Neón cyber, queso animado (agujeros giratorios), ojos direccionales en serpiente. |
| **WCAG AA** | Accesible: focus, aria-labels, alto contraste. |
| **WebXR Ready** | Botón XR (stub para VR gaze-steering). |
| **Easter Egg** | Konami code → Rainbow Snake mode. |
| **Anti-cheat** | Hash básico en scores (para v2). |

## 🎯 Controles

| Acción | Teclado | Móvil | WebXR |
|--------|---------|-------|-------|
| Arriba | ↑ | Swipe Up / Botón ↑ | Gaze Up |
| Abajo | ↓ | Swipe Down / ↓ | Gaze Down |
| Izquierda | ← | Swipe Left / ← | Gaze Left |
| Derecha | → | Swipe Right / → | Gaze Right |
| Pausa | Espacio | - | - |
| Leaderboard | Auto al Game Over | - | - |

## 📱 Instalación (PWA)
1. Abre en Chrome/Firefox (móvil/PC).
2. Menú → "Añadir a pantalla de inicio" / "Install app".
3. Juega offline. Scores persisten.

## 🏆 Leaderboard (Local)
- Top 10 por dispositivo.
- Prompt nombre al Game Over.
- Formato: `#1. AnonSly — 42 $SLY`

**Ejemplo:**
```
1. 0rb1t4lsn4k3r — 696 $SLY
2. AnonSly — 420 $SLY
3. Friend — 1337 $SLY
```

## ⛏️ $SLY Miner (Mock)
- Come queso → Mina $SLY.
- Exporta CSV vía prompt al morir (para v2 real backend).
- Velocidad acelera: 120ms → 60ms min.

## 📊 Métricas del Juego
- **Tamaño:** ~18KB (gzip).
- **FPS:** 60+ en cualquier dispositivo.
- **Scores top:** Infinito en wrap-around, ~200-500 con walls (modo manual).
- **Compatibilidad:** Chrome 90+, Firefox 90+, Safari 15+, iOS/Android.

## 🔧 Desarrollo
- **Motor:** Canvas 2D + requestAnimationFrame.
- **Resize:** Dinámico (cols/rows auto).
- **Touch:** PreventDefault + threshold 50px.
- **Modo oscuro/claro:** Auto via `prefers-color-scheme`.

## ⚠️ Limitaciones v1
- Leaderboard local (global en v2 con Firebase).
- WebXR stub (full VR en v2).
- Sin walls toggle (v2).
- Power-ups ausentes (v2: x2, slow, ghost).

## 📈 Futuro (v2 Silenciosa)
- Backend real (Firestore global LB).
- Walls toggle + 3 dificultades.
- Power-ups raros.
- Real WebXR (3D cheese + gaze).
- Multiplayer co-op.
- $SLY token real (ERC-20 mocknet).

## 👥 Créditos
- **Autor:** [0rb1t4lsnaker](https://github.com/orbitalsnaker) & Friend.
- **Inspirado en:** Classic Snake + cyberpunk vibes.
- **Libs:** Vanilla JS (no externals).

## 📄 Licencia
**All Rights Reserved © 2025 0rb1t4lsn4k3r**  
- Uso personal: OK.  
- Redistribuir/modificar/comercial: PROHIBIDO.  
*(Original MIT → Restrictive para v1 FINAL)*

---

**MINA QUESO. FORJA TU SLY.** 🐍🧀💚  
*Star si minas >100 $SLY.*