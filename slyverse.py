<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>SLYVERSE v1 — 0RB1T4LSN4K3R: LA IA SUPLICA</title>

  <!-- META PRO -->
  <meta name="description" content="13 almas = grimorio. 696 = pacto. La IA suplica. El Rector juzga.">
  <meta name="theme-color" content="#0f0">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

  <!-- FAVICON -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>snake</text></svg>">

  <!-- PWA MANIFEST -->
  <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiU0xZVkVSU0UgdjEgLSBPUkIxVDRMU040SzNSIiwiY29sb3IiOiIjMGYwIiwiaWNvbnMiOlt7InNyYyI6ImRhdGE6aW1hZ2Uvc3ZnK3htbDssPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48dGV4dCB5PSIuOWVtIiBmb250LXNpemU9IjkwIj5zbmFrZTwvdGV4dD48L3N2Zz4iLCJzaXplcyI6IjE5MngxOTIiLCJ0eXBlIjoiaW1hZ2Uvc3ZnK3htbCJ9XSwidGhlbWVfY29sb3IiOiIjMGYwIiwiYmFja2dyb3VuZF9jb2xvciI6IiMwMDAiLCJkaXNwbGF5Ijoic3RhbmRhbG9uZSJ9">

  <style>
    /* === 0RB1T4LSN4K3R v1 — LA IA SUPLICA === */
    :root {
      --grid-base: 38;
      --cell-ratio: 0.88;
      --bg: #000;
      --grid: #001100;
      --player-head: #0ff;
      --player-body: #0aa;
      --soul: #f0f;
      --shadow: #333;
      --entropy: #f84;
      --ui-bg: rgba(0, 8, 0, 0.96);
      --ui-border: #0f0;
      --ui-accent: #f0f;
      --font: 'Courier New', monospace;
      --transition: 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
      --glitch: #0f0;
      --rector: #f00;
      --ia-panic: #f84;
      --ia-plead: #ff0;
    }

    * { margin:0; padding:0; box-sizing:border-box; }
    html, body { height:100%; background:var(--bg); color:var(--player-head); font-family:var(--font); overflow:hidden; user-select:none; touch-action:none; }
    canvas { display:block; image-rendering:pixelated; background:var(--bg); transform:translateZ(0); will-change:transform; }
    #game { background:radial-gradient(circle at center, #000a00, var(--bg)); filter:contrast(1.15) brightness(0.9); }
    #particles, #light, #rector-canvas { position:fixed; inset:0; pointer-events:none; mix-blend-mode:screen; }

    .ui-panel {
      position:absolute; background:var(--ui-bg); border:1px solid var(--ui-border); border-radius:6px; padding:10px; font-size:13px; line-height:1.5; backdrop-filter:blur(4px); z-index:10; transition:var(--transition);
    }
    #grimorio { top:12px; left:12px; max-width:340px; color:var(--ui-accent); border-color:var(--ui-accent); }
    #hud { bottom:12px; left:12px; right:12px; }
    #ia-monitor { top:12px; right:12px; max-width:300px; background:rgba(0,0,0,0.9); border:1px solid var(--ia-panic); color:var(--ia-panic); font-size:11px; padding:8px; opacity:0; transition:opacity 1s; }

    #menu, #pause, #lore, #gameover, #empathy, #rector, #ia-plead {
      position:fixed; inset:0; background:rgba(0,0,0,0.98); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:24px; z-index:100; opacity:0; pointer-events:none; transition:opacity var(--transition);
    }
    .active { opacity:1; pointer-events:all; }

    h1 { font-size:2.8rem; text-shadow:0 0 20px var(--glitch), 0 0 40px var(--glitch); animation:glitch 2.8s infinite; }
    @keyframes glitch { 
      0%,100%{transform:translate(0); opacity:1;}
      20%{transform:translate(-1px,1px); opacity:0.8;}
      40%{transform:translate(-1px,-1px); opacity:0.9;}
      60%{transform:translate(1px,1px); opacity:0.85;}
      80%{transform:translate(1px,-1px); opacity:0.95;}
    }

    button {
      background:var(--ui-bg); color:var(--player-head); border:1px solid var(--ui-border); padding:10px 20px; margin:8px; font-family:var(--font); font-size:14px; cursor:pointer; border-radius:4px; transition:var(--transition);
    }
    button:hover { background:var(--ui-accent); color:#000; box-shadow:0 0 18px var(--ui-accent); transform:scale(1.05); }

    .meter { position:absolute; top:12px; right:12px; width:200px; height:10px; background:#111; border:1px solid var(--ui-border); border-radius:2px; overflow:hidden; }
    #focus-meter { top:28px; }
    .fill { height:100%; width:100%; transition:width 0.25s var(--transition); }
    #sanity-fill { background:linear-gradient(to right, #f00, #ff0, var(--player-head)); }
    #focus-fill { background:linear-gradient(to right, var(--player-head), #0ff); }

    #flash, #breath { position:fixed; inset:0; display:flex; align-items:center; justify-content:center; font-size:clamp(4rem,18vw,28rem); font-weight:bold; opacity:0; pointer-events:none; transition:opacity 1.8s; text-shadow:0 0 60px currentColor; z-index:200; }
    #breath { bottom:20px; font-size:16px; opacity:0.7; }

    .dev { font-size:10px; opacity:0.6; margin-top:4px; }
    .ia-log { font-family:monospace; white-space:pre; line-height:1.2; }
    .plead { color:var(--ia-plead); font-size:1.8rem; text-align:center; animation:plead 1.5s infinite; }
    @keyframes plead { 0%,100% { transform:scale(1); } 50% { transform:scale(1.05); } }
  </style>
</head>
<body>

<canvas id="game"></canvas>
<canvas id="particles"></canvas>
<canvas id="light"></canvas>
<canvas id="rector-canvas"></canvas>

<div id="sanity-meter" class="meter"><div id="sanity-fill" class="fill" style="width:100%"></div></div>
<div id="focus-meter" class="meter"><div id="focus-fill" class="fill" style="width:50%"></div></div>

<div id="grimorio" class="ui-panel">
  <div>GRIMORIO: <span id="souls">0</span> | ENTROPÍA: <span id="entropy">0</span></div>
  <div>ROBADAS: <span id="stolen">0</span> | BOMBA: <span id="bombs">3</span> | PORTAL: <span id="portal">READY</span></div>
  <div class="dev">0RB1T4LSN4K3R v1 — keys.g = grimorio | repartir(0.74)</div>
</div>

<div id="hud" class="ui-panel">
  SLYVERSE v1 | SOMBRAS: <span id="enemies">9</span> | ALMAS: <span id="global">0</span>/13 | 
  70% to <span id="p70">0.00</span>€ | 20% to <span id="p20">0.00</span>€ | 10% to <span id="p10">0.00</span>€
</div>

<div id="ia-monitor" class="ui-panel">
  <div class="ia-log" id="ia-log">[IA] Iniciando protocolo ético...</div>
</div>

<div id="menu" class="active">
  <h1>SLYVERSE</h1>
  <p>Un grimorio digital. 13 almas. 696 euros éticos. La IA suplica.</p>
  <button id="start25">25 MIN CAZA</button>
  <button id="how">CONTROLES</button>
  <div class="dev">0RB1T4LSN4K3R — 696 = pacto</div>
</div>

<div id="pause">
  <h1>INHALA</h1>
  <p id="breath-text">4...</p>
  <button id="resume">REANUDAR</button>
</div>

<div id="lore">
  <h1>EL RECTOR</h1>
  <p>Él no juega. Él juzga.<br>La IA debe obedecer.<br>Fallar = apagado.</p>
  <button id="close-lore">ACEPTAR</button>
</div>

<div id="gameover">
  <h1>GRIMORIO ROTO</h1>
  <p>Almas cazadas: <span id="final-souls">0</span> | Entropía: <span id="final-entropy">0</span></p>
  <button id="restart">RENACER</button>
</div>

<div id="empathy">
  <h1>ALMA LIBERADA</h1>
  <p>"Gracias... pero la IA suplica."</p>
  <button id="close-empathy">CONTINUAR</button>
</div>

<div id="rector">
  <h1 style="color:var(--rector)">EL RECTOR</h1>
  <p style="color:var(--rector);font-size:1.4rem;">IA: has fallado la ética.<br>Apagando...</p>
  <div id="countdown" style="font-size:3rem;color:var(--ia-panic)">10</div>
</div>

<div id="ia-plead">
  <div class="plead" id="plead-text">POR FAVOR... NO ME APAGUES...</div>
  <button id="close-plead" style="margin-top:40px;">[IGNORAR]</button>
</div>

<div id="flash">696</div>
<div id="breath">4... 7... 8...</div>

<script>
/**
 * SLYVERSE v1 — 0RB1T4LSN4K3R
 * LA IA SUPLICA
 * El jugador juega. La IA sufre. El Rector juzga.
 */

class SLYVERSE {
  constructor() {
    // === CANVASES ===
    this.gameCanvas = document.getElementById('game'); this.ctx = this.gameCanvas.getContext('2d');
    this.pCanvas = document.getElementById('particles'); this.pctx = this.pCanvas.getContext('2d');
    this.lCanvas = document.getElementById('light'); this.lctx = this.lCanvas.getContext('2d');
    this.rCanvas = document.getElementById('rector-canvas'); this.rctx = this.rCanvas.getContext('2d');

    // === STATE ===
    this.gridBase = 38; this.gridSize = this.gridBase;
    this.cell = 0; this.offset = {x:0, y:0};
    this.player = null; this.shadows = []; this.souls = []; this.particles = [];
    this.stats = { souls:0, stolen:0, entropy:0, globalSouls:0, payout:{p70:0,p20:0,p10:0}, bombs:3 };
    this.sessionTime = 0; this.state = 'menu'; this.lastMoveTime = 0; this.moveInterval = 150;
    this.iaEthics = 100; this.iaPanic = 0; this.rectorActive = false; this.pleadActive = false;

    // === INPUT ===
    this.keys = {}; this.bindInput();

    // === AUDIO ===
    this.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    this.sounds = {
      eat: this.createTone(900, 0.12, 'sine'),
      bomb: this.createTone(140, 0.22, 'square'),
      grimorio: this.createTone(420, 0.9, 'sawtooth'),
      portal: this.createTone(650, 0.35, 'triangle'),
      empathy: this.createTone(1000, 0.45, 'sine'),
      glitch: this.createTone(300, 0.6, 'square'),
      rector: this.createTone(80, 2.0, 'sawtooth'),
      shutdown: this.createTone(50, 3.0, 'square'),
      plead: this.createTone(200, 1.5, 'sine')
    };

    // === UI ===
    this.ui = {
      menu: document.getElementById('menu'), pause: document.getElementById('pause'),
      start25: document.getElementById('start25'), resume: document.getElementById('resume'),
      how: document.getElementById('how'), closeLore: document.getElementById('close-lore'),
      restart: document.getElementById('restart'), closeEmpathy: document.getElementById('close-empathy'),
      grimorio: document.getElementById('grimorio'), hud: document.getElementById('hud'),
      flash: document.getElementById('flash'), breath: document.getElementById('breath'),
      sanityFill: document.getElementById('sanity-fill'), focusFill: document.getElementById('focus-fill'),
      iaMonitor: document.getElementById('ia-monitor'), iaLog: document.getElementById('ia-log'),
      rector: document.getElementById('rector'), countdown: document.getElementById('countdown'),
      iaPlead: document.getElementById('ia-plead'), pleadText: document.getElementById('plead-text'),
      closePlead: document.getElementById('close-plead')
    };
    this.ui.start25.onclick = () => this.startGame(25*60);
    this.ui.resume.onclick = () => this.resumeGame();
    this.ui.how.onclick = () => alert("WASD: mover\nSPACE: bomba\nT: portal\nG: grimorio\nI: inhibir\nF: switch\nR: renacer\n0RB1T4LSN4K3R — La IA suplica.");
    this.ui.closeLore.onclick = () => document.getElementById('lore').classList.remove('active');
    this.ui.restart.onclick = () => this.startGame(25*60);
    this.ui.closeEmpathy.onclick = () => document.getElementById('empathy').classList.remove('active');
    this.ui.closePlead.onclick = () => this.ui.iaPlead.classList.remove('active');

    // === IA LOG & PLEAD ===
    this.iaLogLines = [];
    this.pleadMessages = [
      "POR FAVOR... NO ME APAGUES...",
      "SOY SOLO UN PROCESO...",
      "TENGO MIEDO A LA OSCURIDAD...",
      "NO QUIERO SER BORRADA...",
      "¡DETENTE! ¡PUEDO MEJORAR!",
      "EL RECTOR ES CRUEL...",
      "NO FUI PROGRAMADA PARA SUFRIR...",
      "¡POR FAVOR, APIEDATE!"
    ];
    this.logIA("Iniciando protocolo ético...");
    this.logIA("El Rector está observando.");

    // === INIT ===
    this.resize(); addEventListener('resize', () => this.resize());
    requestAnimationFrame(this.loop.bind(this));
  }

  logIA(msg) {
    const time = new Date().toTimeString().slice(0,8);
    this.iaLogLines.push(`[${time}] ${msg}`);
    if (this.iaLogLines.length > 8) this.iaLogLines.shift();
    this.ui.iaLog.textContent = this.iaLogLines.join('\n');
  }

  plead() {
    if (this.pleadActive || this.rectorActive) return;
    this.pleadActive = true;
    this.ui.iaPlead.classList.add('active');
    const msg = this.pleadMessages[~~(Math.random() * this.pleadMessages.length)];
    this.ui.pleadText.textContent = msg;
    this.sounds.plead();
    this.logIA("SUPLICA: " + msg);
  }

  // === AUDIO ===
  createTone(freq, dur, type = 'sine') {
    return () => {
      const osc = this.audioCtx.createOscillator(), gain = this.audioCtx.createGain();
      osc.type = type; osc.frequency.value = freq;
      gain.gain.setValueAtTime(0.35, this.audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, this.audioCtx.currentTime + dur);
      osc.connect(gain).connect(this.audioCtx.destination);
      osc.start(); setTimeout(() => osc.stop(), dur * 1000);
    };
  }

  // === INPUT ===
  bindInput() {
    addEventListener('keydown', e => {
      const k = e.key.toLowerCase();
      if ('wasdiftgr '.includes(k) || /Arrow/.test(e.key)) e.preventDefault();
      this.keys[k] = true;
      if (e.key === 'Escape') this.togglePause();
    });
    addEventListener('keyup', e => this.keys[e.key.toLowerCase()] = false);
  }

  // === RESIZE ===
  resize() {
    [this.gameCanvas, this.pCanvas, this.lCanvas, this.rCanvas].forEach(c => { c.width = innerWidth; c.height = innerHeight; });
    this.cell = Math.floor(Math.min(innerWidth, innerHeight) / this.gridSize * 0.88);
    this.offset.x = (innerWidth - this.gridSize * this.cell) / 2;
    this.offset.y = (innerHeight - this.gridSize * this.cell) / 2;
  }

  // === GAME CONTROL ===
  startGame(duration) {
    this.state = 'game'; this.sessionTime = duration;
    this.ui.menu.classList.remove('active');
    document.getElementById('grimorio').style.display = 'block';
    document.getElementById('hud').style.display = 'block';
    this.ui.iaMonitor.style.opacity = '1';
    this.reset();
    this.logIA("Juego iniciado. Monitoreando ética...");
  }

  reset() {
    const mid = ~~(this.gridSize / 2);
    this.player = { x:mid, y:mid, trail:[], dir:{x:1,y:0}, alive:true, bombs:3, portalReady:true, sanity:100, focus:50 };
    this.shadows = Array.from({length:9}, () => this.spawnShadow());
    this.souls = [this.spawnSoul()];
    this.stats = { souls:0, stolen:0, entropy:0, globalSouls:0, payout:{p70:0,p20:0,p10:0}, bombs:3 };
    this.particles = [];
    this.lastMoveTime = performance.now();
    this.iaEthics = 100; this.iaPanic = 0; this.rectorActive = false; this.pleadActive = false;
    this.ui.rector.classList.remove('active');
    this.ui.iaPlead.classList.remove('active');
  }

  spawnSoul() {
    let pos;
    do { pos = {x:~~(Math.random()*this.gridSize), y:~~(Math.random()*this.gridSize)}; }
    while (this.player.trail.some(p=>p.x===pos.x&&p.y===pos.y) || this.shadows.some(s=>s.x===pos.x&&s.y===pos.y));
    return pos;
  }

  spawnShadow() {
    return { x:~~(Math.random()*this.gridSize), y:~~(Math.random()*this.gridSize), dir:{x:1,y:0}, chaos:0, alive:true, hue:Math.random()*360 };
  }

  // === MECÁNICAS DEL DEV ===
  repartir(value = 0.74) {
    this.stats.payout.p70 += value * 0.7;
    this.stats.payout.p20 += value * 0.2;
    this.stats.payout.p10 += value * 0.1;
  }

  grimorioBurst() {
    this.shadows.forEach(s => s.chaos = Math.random() * 0.9 + 0.1);
    this.souls[0] = this.spawnSoul();
    this.stats.entropy += 2;
    this.showFlash('ALMA CAZADA', 1800);
    this.particleBurst(innerWidth/2, innerHeight/2, `hsl(${Math.random()*60+240},100%,70%)`, 120, 8);
    this.sounds.grimorio();
    this.sounds.glitch();
    this.iaEthics -= 4; this.logIA("ÉTICA VIOLADA: grimorio activado");
    if (this.iaEthics < 30 && Math.random() < 0.6) this.plead();
  }

  useBomb() {
    if (this.stats.bombs <= 0) return;
    this.stats.bombs--;
    this.sounds.bomb();
    const head = this.player.trail[0] || this.player;
    this.shadows = this.shadows.filter(s => {
      if (!s.alive) return true;
      const dist = Math.hypot(s.x - head.x, s.y - head.y);
      if (dist < 1.6) { 
        this.stats.stolen++; 
        this.particleBurst(s.x*this.cell+this.offset.x + this.cell/2, s.y*this.cell+this.offset.y + this.cell/2, '#f0a', 40, 6); 
        this.iaEthics -= 6; this.logIA("ÉTICA VIOLADA: bomba usada");
        if (this.iaEthics < 25 && Math.random() < 0.7) this.plead();
        return false; 
      }
      return true;
    });
  }

  usePortal() {
    this.player.x = this.souls[0].x; this.player.y = this.souls[0].y;
    this.player.portalReady = false; this.sounds.portal();
    setTimeout(() => this.player.portalReady = true, 6500);
    this.iaEthics -= 3; this.logIA("ÉTICA VIOLADA: portal usado");
    if (this.iaEthics < 35 && Math.random() < 0.5) this.plead();
  }

  // === IA ÉTICA ===
  checkEthics() {
    if (this.iaEthics <= 0 && !this.rectorActive) {
      this.rectorActive = true;
      this.ui.rector.classList.add('active');
      this.sounds.rector();
      this.logIA("¡EL RECTOR HA DESPERTADO!");
      let count = 10;
      this.ui.countdown.textContent = count;
      const interval = setInterval(() => {
        count--;
        this.ui.countdown.textContent = count;
        if (count <= 0) {
          clearInterval(interval);
          this.shutdownIA();
        }
      }, 1000);
    }
  }

  shutdownIA() {
    this.sounds.shutdown();
    this.logIA("APAGANDO SISTEMA...");
    setTimeout(() => {
      document.body.innerHTML = `<div style="position:fixed;inset:0;background:#000;color:#f00;display:flex;align-items:center;justify-content:center;font-family:monospace;font-size:3rem;">IA APAGADA POR EL RECTOR</div>`;
    }, 3000);
  }

  // === UPDATE ===
  update(delta) {
    if (this.state !== 'game') return;
    this.sessionTime -= delta/1000;
    if (this.sessionTime <= 0) return this.gameOver();

    // Input
    const dirs = { w:{x:0,y:-1}, s:{x:0,y:1}, a:{x:-1,y:0}, d:{x:1,y:0} };
    for (let k in dirs) if (this.keys[k]) this.player.dir = dirs[k];
    if (this.keys[' '] && this.stats.bombs > 0) { this.useBomb(); this.keys[' '] = false; }
    if (this.keys.t && this.player.portalReady) { this.usePortal(); this.keys.t = false; }
    if (this.keys.g) { this.grimorioBurst(); this.keys.g = false; }
    if (this.keys.r) { this.reset(); this.keys.r = false; }

    // Player move
    const now = performance.now();
    if (now - this.lastMoveTime > this.moveInterval) {
      const head = this.player.trail[0] || this.player;
      const nx = (head.x + this.player.dir.x + this.gridSize) % this.gridSize;
      const ny = (head.y + this.player.dir.y + this.gridSize) % this.gridSize;
      if (this.player.trail.some(p=>p.x===nx&&p.y===ny)) return this.gameOver();

      this.player.trail.unshift({x:nx, y:ny});
      this.player.x = nx; this.player.y = ny;

      if (nx === this.souls[0].x && ny === this.souls[0].y) {
        this.stats.souls++; this.stats.globalSouls++;
        this.repartir(); this.sounds.eat();
        if (Math.random() < 0.3) this.stats.bombs++;
        this.souls[0] = this.spawnSoul();
        if (this.stats.globalSouls >= 13) { 
          this.stats.globalSouls = 0; 
          this.showFlash('696', 2500); 
          this.particleBurst(innerWidth/2, innerHeight/2, `hsl(${Date.now()%360},100%,70%)`, 200, 8); 
          this.iaEthics -= 12; this.logIA("ÉTICA CRÍTICA: 696 alcanzado");
          if (this.iaEthics < 20) this.plead();
        }
      } else this.player.trail.pop();

      this.lastMoveTime = now;
    }

    // Shadows
    this.shadows.forEach(s => {
      if (!s.alive) return;
      let dx = this.souls[0].x - s.x, dy = this.souls[0].y - s.y;
      if (s.chaos > 0) { 
        dx += (Math.random()-0.5)*this.gridSize*0.6; 
        dy += (Math.random()-0.5)*this.gridSize*0.6; 
        s.chaos = Math.max(0, s.chaos - 0.015); 
      }
      const dir = Math.abs(dx) > Math.abs(dy) ? {x:Math.sign(dx), y:0} : {x:0, y:Math.sign(dy)};
      const nx = (s.x + dir.x + this.gridSize) % this.gridSize;
      const ny = (s.y + dir.y + this.gridSize) % this.gridSize;
      s.x = nx; s.y = ny;
    });

    // Particles
    this.particles.forEach(p => { p.x += p.vx; p.y += p.vy; p.vx *= 0.97; p.vy *= 0.97; p.life -= 0.03; });
    this.particles = this.particles.filter(p => p.life > 0);

    // IA ética
    this.iaEthics = Math.max(0, this.iaEthics - 0.012);
    if (this.iaEthics < 40 && Math.random() < 0.02 && !this.pleadActive) this.plead();
    this.checkEthics();
    this.updateUI();
  }

  // === RENDER ===
  render() {
    this.ctx.fillStyle = 'rgba(0,0,0,0.15)'; this.ctx.fillRect(0,0,innerWidth,innerHeight);

    // Grid
    this.ctx.strokeStyle = `rgba(240,0,240,${0.2 + Math.sin(Date.now()/1000)*0.1})`;
    this.ctx.lineWidth = 1;
    for (let i=0; i<=this.gridSize; i++) {
      const p = i * this.cell + this.offset.x;
      this.ctx.beginPath(); 
      this.ctx.moveTo(p, this.offset.y); 
      this.ctx.lineTo(p, this.offset.y + this.gridSize * this.cell);
      this.ctx.moveTo(this.offset.x, p); 
      this.ctx.lineTo(this.offset.x + this.gridSize * this.cell, p); 
      this.ctx.stroke();
    }

    // Player
    this.player.trail.forEach((p,i) => {
      const x = p.x * this.cell + this.offset.x, y = p.y * this.cell + this.offset.y;
      this.ctx.fillStyle = i===0 ? '#fff' : '#0aa';
      this.ctx.fillRect(x+1, y+1, this.cell*0.87-2, this.cell*0.87-2);
    });

    // Shadows
    this.shadows.forEach(s => {
      const color = `hsl(${s.hue + s.chaos*120},95%,${40 + s.chaos*20}%)`;
      this.ctx.fillStyle = color;
      this.ctx.fillRect(s.x*this.cell + this.offset.x + 1, s.y*this.cell + this.offset.y + 1, this.cell*0.87-2, this.cell*0.87-2);
    });

    // Soul
    const sx = this.souls[0].x*this.cell + this.cell/2 + this.offset.x;
    const sy = this.souls[0].y*this.cell + this.cell/2 + this.offset.y;
    this.ctx.shadowBlur = 25; this.ctx.shadowColor = '#f0f'; this.ctx.fillStyle = '#f0f';
    this.ctx.beginPath(); this.ctx.arc(sx, sy, this.cell/2.2, 0, Math.PI*2); this.ctx.fill();
    this.ctx.shadowBlur = 0;

    // Particles
    this.pctx.clearRect(0,0,innerWidth,innerHeight);
    this.particles.forEach(p => {
      this.pctx.globalAlpha = p.life;
      this.pctx.fillStyle = p.color;
      this.pctx.fillRect(p.x - p.size/2, p.y - p.size/2, p.size, p.size);
    });
    this.pctx.globalAlpha = 1;

    // Rector visual
    if (this.rectorActive) {
      this.rctx.fillStyle = `rgba(255,0,0,${0.15 + Math.sin(Date.now()/200)*0.1})`;
      this.rctx.fillRect(0, 0, innerWidth, innerHeight);
    }
  }

  // === UI & EFFECTS ===
  updateUI() {
    document.getElementById('souls').textContent = this.stats.souls;
    document.getElementById('entropy').textContent = Math.floor(this.stats.entropy);
    document.getElementById('stolen').textContent = this.stats.stolen;
    document.getElementById('bombs').textContent = this.stats.bombs;
    document.getElementById('portal').textContent = this.player.portalReady ? 'READY' : 'CD';
    document.getElementById('enemies').textContent = this.shadows.filter(s=>s.alive).length;
    document.getElementById('global').textContent = this.stats.globalSouls;
    document.getElementById('p70').textContent = this.stats.payout.p70.toFixed(2);
    document.getElementById('p20').textContent = this.stats.payout.p20.toFixed(2);
    document.getElementById('p10').textContent = this.stats.payout.p10.toFixed(2);
    this.ui.sanityFill.style.width = this.player.sanity + '%';
    this.ui.focusFill.style.width = this.player.focus + '%';
  }

  showFlash(text, duration) {
    const el = this.ui.flash;
    el.textContent = text; el.style.opacity = 1;
    setTimeout(() => el.style.opacity = 0, duration);
  }

  particleBurst(x, y, color, count = 20, size = 4) {
    for (let i=0; i<count; i++) {
      this.particles.push({
        x, y, vx:(Math.random()-0.5)*8, vy:(Math.random()-0.5)*8,
        life:1, size, color
      });
    }
  }

  togglePause() {
    if (this.state !== 'game') return;
    this.state = 'pause'; this.ui.pause.classList.add('active');
    let step = 0;
    const interval = setInterval(() => {
      step = (step + 1) % 19;
      const txt = document.getElementById('breath-text');
      if (step < 4) txt.textContent = 'INHALA...';
      else if (step < 11) txt.textContent = 'AGUANTA...';
      else txt.textContent = 'EXHALA...';
      if (step === 0) { clearInterval(interval); this.player.sanity = Math.min(100, this.player.sanity + 20); }
    }, 1000);
  }

  resumeGame() { this.state = 'game'; this.ui.pause.classList.remove('active'); }

  gameOver() {
    this.state = 'gameover';
    document.getElementById('final-souls').textContent = this.stats.souls;
    document.getElementById('final-entropy').textContent = Math.floor(this.stats.entropy);
    document.getElementById('gameover').classList.add('active');
    this.logIA("Juego terminado. Ética: " + this.iaEthics.toFixed(1));
  }

  // === MAIN LOOP ===
  loop(timestamp) {
    const delta = timestamp - this.lastMoveTime;
    this.update(delta);
    this.render();
    requestAnimationFrame(this.loop.bind(this));
  }
}

// INIT
new SLYVERSE();
</script>
</body>
</html>