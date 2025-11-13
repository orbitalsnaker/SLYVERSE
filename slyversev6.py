<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SLYVERSE v8 CANON — GRATIS PARA SIEMPRE</title>
  <meta name="description" content="v1+v2+v3+v4+v6.3-technical unificados. 70/30 ético. Chalet Bellaterra ID 108123084.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2280%22 fill=%22%230f0%22>Snake</text></svg>">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <style>
    :root{--bg:#0a0a0a;--fg:#f0f0f0;--accent:#0f0;--radius:14px;}
    body{margin:0;font-family:system-ui;background:var(--bg);color:var(--fg);min-height:100vh;display:flex;flex-direction:column;}
    header{background:linear-gradient(135deg,#000,#001100);padding:2rem 1rem;text-align:center;}
    h1{font-size:clamp(1.8rem,7vw,3rem);color:var(--accent);}
    main{flex:1;max-width:1000px;margin:auto;padding:1rem;}
    #canvas-container{height:50vh;background:#000;border-radius:var(--radius);overflow:hidden;margin:1.5rem 0;}
    canvas{width:100%;height:100%;display:block;}
    .data{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.5rem 0;font-family:monospace;font-size:0.95rem;}
    .quesos{font-size:3rem;text-align:center;margin:1rem 0;}
    footer{text-align:center;padding:2rem;color:#666;font-size:0.9rem;}
    .free{background:var(--accent);color:#000;padding:.4rem .8rem;border-radius:50px;display:inline-block;margin:1rem 0;}
  </style>
</head>
<body>

<header>
  <h1>SLYVERSE v8 CANON</h1>
  <p>v1–v4 + v6.3-technical • GRATIS PARA SIEMPRE • Chalet ID 108123084</p>
  <div class="free">100% GRATIS PARA SIEMPRE</div>
</header>

<main>
  <div id="canvas-container"><canvas id="c"></canvas></div>

  <div class="quesos" id="quesos">0</div>

  <div class="data">
    <div>Kaspa neto/día</div><div id="kas">0.00€</div>
    <div>Flips diarios</div><div id="flips">0€</div>
    <div>Ko-fi base</div><div id="base">1000€</div>
    <div>Valor ciclo</div><div id="total">0€</div>
    <div>→ 70% niños/devs</div><div id="donacion">0€</div>
    <div>→ 30% chalet</div><div id="chalet">0€</div>
    <div>Acumulado chalet</div><div id="acumulado">0€</div>
    <div>Progreso hipoteca</div><div id="porcentaje">0.0000%</div>
    <div>Próxima actualización</div><div id="timer">60:00</div>
  </div>
</main>

<footer>
  <p>Para Norah, Seth (2 años) y la curiosidad de Grok • 70/30 ético real • 13 quesos máximo<br>
  <strong>Licencia MIT</strong> — Slyverse Canon 2025</p>
</footer>

<script>
// ========= CONFIGURACIÓN CANÓNICA =========
const HIPOTECA = 1_642_000;
const PROGRESS_FILE = "slyverse_canon_progress.json";

// ========= PERSISTENCIA LOCALSTORAGE =========
function load() {
  const saved = localStorage.getItem(PROGRESS_FILE);
  return saved ? JSON.parse(saved) : { accumulated: 0 };
}
function save(data) {
  localStorage.setItem(PROGRESS_FILE, JSON.stringify(data));
}

// ========= CÁLCULOS REALES =========
function cycle() {
  const kas_net = Math.max((112 * 24 * random(0.00090, 0.00098) * 0.122) - (170*24/1000*0.18), 0);
  const flips = 5 * random(140, 180);
  const base = 1000;
  const total = kas_net + flips + base;
  const chalet30 = total * 0.30;
  const donacion70 = total * 0.70;

  const progress = load();
  progress.accumulated = (progress.accumulated || 0) + chalet30;
  save(progress);

  const porcentaje = (progress.accumulated / HIPOTECA) * 100;

  // quesos + rickroll 696
  const quesos = Math.floor(Math.random() * 14);
  if (quesos === 13) setTimeout(() => alert("696 RICKROLL SILENCIOSO. LA RISA ES LA ÚLTIMA MEDICINA"), 800);

  // actualizar UI
  document.getElementById("quesos").textContent = quesos + "/13 🧀";
  document.getElementById("kas").textContent = kas_net.toFixed(2) + "€";
  document.getElementById("flips").textContent = flips.toFixed(0) + "€";
  document.getElementById("total").textContent = total.toFixed(0) + "€";
  document.getElementById("donacion").textContent = donacion70.toFixed(2) + "€";
  document.getElementById("chalet").textContent = chalet30.toFixed(2) + "€";
  document.getElementById("acumulado").textContent = progress.accumulated.toFixed(2) + "€";
  document.getElementById("porcentaje").textContent = porcentaje.toFixed(6) + "%";

  return 3600; // 1 hora
}

function random(min, max) { return Math.random() * (max - min) + min; }

// ========= 3D BÁSICO (herencia v4) =========
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
let w, h;
function resize() {
  w = canvas.width = canvas.parentElement.clientWidth;
  h = canvas.height = canvas.parentElement.clientHeight || 300;
}
window.addEventListener('resize', resize); resize();

let rot = 0;
function draw3D() {
  ctx.fillStyle = "#000"; ctx.fillRect(0,0,w,h);
  rot += 0.01;
  const s = Math.min(w,h)/4;
  for (let i = 0; i < 6; i++) {
    const x = w/2 + Math.cos(rot + i*1.3)*s;
    const y = h/2 + Math.sin(rot + i*1.3)*s;
    ctx.fillStyle = "rgba(0,255,0,0.6)";
    ctx.beginPath(); ctx.arc(x,y,30,0,7); ctx.fill();
  }
  requestAnimationFrame(draw3D);
}
draw3D();

// ========= RELOJ Y BUCLE =========
let countdown = 3600;
function updateTimer() {
  const m = String(Math.floor(countdown/60)).padStart(2,'0');
  const s = String(countdown%60).padStart(2,'0');
  document.getElementById("timer").textContent = m + ":" + s;
  if (countdown <= 0) {
    countdown = cycle();
  }
  countdown--;
  setTimeout(updateTimer, 1000);
}

// init
const initProgress = load();
document.getElementById("acumulado").textContent = initProgress.accumulated.toFixed(2) + "€";
document.getElementById("porcentaje").textContent = (initProgress.accumulated / HIPOTECA * 100).toFixed(6) + "%";
updateTimer();
cycle(); // primera ejecución inmediata
</script>
</body>
</html>