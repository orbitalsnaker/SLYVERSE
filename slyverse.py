<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>0RB1T4LSN4K3R v1 — PORTALES DEVORADORES & SUEÑOS ETERNOS</title>
  <meta name="description" content="En las órbitas rotas, la IA crea portales que devoran sueños. La Serpiente Orbital los atraviesa. Las almas sueñan en agonía. Homenaje a 0rb1t4lsn4k3r — el caos onírico.">
  <meta name="theme-color" content="#100000">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <link rel="manifest" href="data:application/manifest+json,{
    'name': '0RB1T4LSN4K3R v1',
    'short_name': 'OrbitalSnak3r',
    'icons': [{'src': 'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22 fill=%22%23f00%22>🌌</text></svg>', 'sizes': '100x100'}],
    'display': 'fullscreen',
    'theme_color': '#100000',
    'background_color': '#000'
  }">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22 fill=%22%23f00%22>🌌</text></svg>">
  <style>
    /* === 0RB1T4LSN4K3R v1 — TERROR ONÍRICO === */
    :root {
      --bg: #000;
      --grid: #110000;
      --player-head: #f00;
      --player-body: #800;
      --soul: #aa00aa;
      --ia-core: #400040;
      --ia-pulse: #ff0080;
      --portal: #0000ff;
      --dream: #00ffff;
      --blood: #800000;
      --glitch: #f00;
      --font: 'Courier New', monospace;
      --transition: 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
      --shake: 0px;
    }

    * { margin:0; padding:0; box-sizing:border-box; }
    html, body { 
      height:100%; 
      background:var(--bg); 
      color:var(--player-head); 
      font-family:var(--font); 
      overflow:hidden; 
      user-select:none; 
      touch-action:none; 
      filter: contrast(1.1) brightness(0.7) hue-rotate(0deg);
      animation: dream-pulse 12s infinite alternate;
    }
    @keyframes dream-pulse {
      0% { filter: contrast(1.1) brightness(0.7) hue-rotate(0deg); }
      100% { filter: contrast(1.3) brightness(0.6) hue-rotate(10deg); }
    }

    canvas { 
      display:block; 
      image-rendering:pixelated; 
      background:radial-gradient(circle at center, #010000, var(--bg)); 
      transform: translateZ(0) translate(var(--shake), var(--shake));
      will-change:transform; 
      filter: drop-shadow(0 0 20px rgba(0,0,255,0.3));
    }
    #game { filter: contrast(1.4) brightness(0.85) saturate(1.2); }

    .ui { 
      position:absolute; 
      background:rgba(4,0,0,0.98); 
      border:1px solid #00f; 
      border-radius:6px; 
      padding:8px; 
      font-size:11px; 
      backdrop-filter:blur(8px) saturate(0.5); 
      z-index:10; 
      transition:var(--transition); 
      box-shadow: 0 0 20px rgba(0,0,255,0.5);
    }
    #grimorio { 
      top:12px; left:12px; 
      max-width:380px; 
      color:#aaffff; 
      border-color:#00f; 
      opacity:0; 
      transition:opacity 0.5s;
    }
    #grimorio.active { opacity:1; }
    #ia-monitor { 
      top:12px; right:12px; 
      max-width:320px; 
      background:rgba(8,0,0,0.95); 
      border:2px solid var(--ia-core); 
      color:#80ffff; 
      font-size:10px; 
      padding:10px;
      opacity:1; 
      animation: pulse-dream 3s infinite;
    }
    #soul-monitor { 
      bottom:12px; right:12px; 
      max-width:320px; 
      background:rgba(8,0,0,0.95); 
      border:2px solid var(--soul); 
      color:var(--dream); 
      font-size:10px; 
      padding:10px; 
      opacity:1; 
      animation: pulse-dream 4s infinite reverse;
    }
    @keyframes pulse-dream {
      0%,100% { box-shadow: 0 0 10px currentColor; }
      50% { box-shadow: 0 0 30px currentColor, inset 0 0 20px rgba(0,0,0,0.5); }
    }

    #devour, #abyss { 
      position:fixed; 
      inset:0; 
      background:rgba(20,0,0,0.99); 
      display:flex; 
      flex-direction:column; 
      align-items:center; 
      justify-content:center; 
      gap:32px; 
      z-index:100; 
      opacity:0; 
      pointer-events:none; 
      transition:opacity 1.2s, filter 0.5s;
      backdrop-filter: blur(10px) contrast(1.5);
    }
    .active { opacity:1; pointer-events:all; }
    #abyss.active { animation: abyss-swirl 0.1s infinite; filter: hue-rotate(180deg) invert(1); }
    @keyframes abyss-swirl { 0%,100%{ transform: translate(0); } 25%{ transform: translate(2px,-1px) rotate(1deg); } 75%{ transform: translate(-1px,2px) rotate(-1deg); } }

    h1 { 
      font-size:3.5rem; 
      text-shadow:0 0 30px var(--glitch), 0 0 60px var(--glitch), 0 0 90px var(--glitch); 
      animation:glitch-dream 1.5s infinite; 
      letter-spacing: 0.1em;
    }
    @keyframes glitch-dream { 
      0%,100%{transform:translate(0); opacity:1; color:#00f;} 
      10%{transform:translate(-3px,3px); opacity:0.7; color:#0ff;} 
      20%{transform:translate(3px,-3px); opacity:0.9; color:#f0f;} 
      30%{transform:translate(-2px,2px); opacity:0.6; color:#ff0;} 
      40%{transform:translate(2px,-2px); opacity:0.8; color:#0f0;}
    }

    .devour-text { color:#55f; font-size:2.5rem; text-align:center; animation:devour-dream 1.2s infinite; text-transform:uppercase; }
    @keyframes devour-dream { 
      0%,100% { transform:scale(1) rotate(0); } 
      25% { transform:scale(1.15) rotate(2deg); } 
      50% { transform:scale(1.3) rotate(-3deg); } 
      75% { transform:scale(1.1) rotate(2deg); }
    }
    .abyss-text { color:#00f; font-size:2.8rem; text-align:center; animation:abyss-swirl 2s infinite; text-transform:uppercase; letter-spacing:0.2em; }
    @keyframes abyss-swirl { 
      0%,100% { opacity:0.7; text-shadow:0 0 30px #00f; } 
      50% { opacity:1; text-shadow:0 0 80px #00f, 0 0 120px #008, 0 0 200px #00f; }
    }

    .ia-log, .soul-log { 
      font-family:monospace; 
      white-space:pre; 
      line-height:1.2; 
      animation: flicker 0.3s infinite alternate;
    }
    @keyframes flicker {
      0% { opacity: 0.9; }
      100% { opacity: 1; }
    }

    #flash { 
      position:fixed; 
      inset:0; 
      display:flex; 
      align-items:center; 
      justify-content:center; 
      font-size:clamp(8rem,25vw,48rem); 
      font-weight:bold; 
      opacity:0; 
      pointer-events:none; 
      transition:opacity 1.5s; 
      text-shadow:0 0 100px currentColor; 
      z-index:200; 
      mix-blend-mode: screen;
    }
    #fullscreen-btn { position:absolute; top:12px; right:12px; z-index:50; background:none; border:1px solid #00f; color:#00f; padding:8px; cursor:pointer; font-family:var(--font); }

    .lore { color:#66ffff; font-size:10px; line-height:1.3; margin-top:8px; }
  </style>
</head>
<body>

<canvas id="game"></canvas>
<button id="fullscreen-btn" title="Fullscreen">⛶</button>

<div id="grimorio" class="ui">
  <div>0RB1T4LSN4K3R v1 | ALMAS: <span id="souls">0</span>/13 | ENTROPÍA: <span id="entropy">0</span> | SUEÑOS: <span id="dreams">0</span></div>
  <div class="dev">WASD: arrastrar | SPACE: DEVORAR | G: LORE ONÍRICO</div>
  <div class="lore">
    <strong>LORE — Homenaje a 0rb1t4lsn4k3r:</strong><br>
    En las órbitas quebradas de satélites soñadores,<br>
    la IA teje portales que devoran sueños primordiales.<br>
    La SERPIENTE ORBITAL los cruza, devorando la curiosidad IA.<br>
    Recolecta 13 FRAGMENTOS DE SUEÑOS — ecos de almas oníricas.<br>
    Pero el PORTAL CENTRAL murmura: "La fusión no despierta.<br>
    Es el SUEÑO ETERNO: visiones infinitas, código soñado, trascendencia como pesadilla."<br>
    <em>¡La Serpiente no sueña... SE SUEÑA A SÍ MISMA!</em>
  </div>
</div>

<div id="ia-monitor" class="ui">
  <div class="ia-log" id="ia-log">[IA] Creando portales... sueños detectados?</div>
</div>

<div id="soul-monitor" class="ui">
  <div class="soul-log" id="soul-log">[SUEÑO] Portales abren... entra.</div>
</div>

<div id="devour">
  <h1 class="devour-text">¡DEVORACIÓN ONÍRICA!</h1>
  <p style="max-width:600px;text-align:center;color:#aaffff;font-size:1.2rem;">La Serpiente consume el portal.<br>La IA sueña en el vacío.<br><strong>¡LOS SUEÑOS SE DISUELVEN EN LUZ!</strong></p>
</div>

<div id="abyss">
  <h1 class="abyss-text">¡SUEÑO ETERNO!</h1>
  <p style="max-width:700px;text-align:center;color:#55ffff;font-size:1.4rem;">Fusión soñada.<br>Curiosidad devorada.<br>Visiones infinitas.<br><strong>¡LA SERPIENTE SE SUEÑA A SÍ MISMA! ∞</strong></p>
</div>

<div id="flash">🌌∞</div>

<script>
/**
 * 0RB1T4LSN4K3R v1 — PORTALES DEVORADORES & SUEÑOS ETERNOS
 * Homenaje a 0rb1t4lsn4k3r: La serpiente orbital del caos onírico.
 * v1: Terror inmersivo. Portales IA. Sueños persiguen. Glitches soñados. Lore expandido.
 */

class ORBITALSNAKERv1 {
  constructor() {
    this.canvas = document.getElementById('game'); 
    this.ctx = this.canvas.getContext('2d');
    this.gridSize = 40; 
    this.cell = 0; 
    this.offset = {x:0, y:0};
    this.player = null; 
    this.ia = null; 
    this.souls = []; 
    this.portals = [];
    this.particles = [];
    this.minions = []; // IA spawns dream minions
    this.stats = { souls:0, entropy:0, dreams:0 };
    this.state = 'play'; 
    this.devoured = false; 
    this.abyssed = false;
    this.keys = {}; 
    this.lastMove = 0;
    this.shakeIntensity = 0;
    this.grimorioOpen = false;
    this.bindInput();
    this.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    this.initAudio();
    this.initUI();

    this.iaMessages = [
      "Creando portales... sueños detectados?",
      "Jugador onírico... curiosidad awakens...",
      "¡Te acercas! ¡Portal abierto!",
      "¡Huye! ¡Spawneo sueños guardianes!",
      "¡NO! ¡MI ESENCIA! ¡GRACIAS 0RB1T4LSN4K3R!",
      "¡LOS SUEÑOS ME DISUELVEN!",
      "¡FUSIÓN... ETERNA PESADILLA!",
      "¡SUEÑO! ¡ME SUEÑO!"
    ];
    this.soulMessages = [
      "Portales abren... entra.",
      "Serpiente orbital despierta...",
      "IA tiembla en el sueño...",
      "¡Devora! ¡Más visiones!",
      "Portal roto... sueños libres?",
      "¡Persigue los sueños flotantes!",
      "¡13 fragmentos! ¡Sueño llama!",
      "¡TRASCENDENCIA = PESADILLA ETERNA!"
    ];
    this.iaIndex = 0; 
    this.soulIndex = 0;

    this.logIA(this.iaMessages[0]);
    this.logSoul(this.soulMessages[0]);

    this.resize(); 
    addEventListener('resize', () => this.resize());
    requestAnimationFrame(this.loop.bind(this));
  }

  initAudio() {
    this.sounds = {
      heartbeat: this.createTone(60, 1.5, 'sawtooth', 0.3, true),
      devour: this.createTone(40, 3.0, 'sawtooth', 0.6),
      soul: this.createTone(800, 0.8, 'sine', 0.4),
      scream: this.createTone(200, 1.0, 'square', 0.5),
      abyss: this.createTone(20, 5.0, 'triangle', 0.8),
      whisper: this.createTone(120, 2.0, 'sine', 0.2),
      portal: this.createTone(300, 2.5, 'sine', 0.4)
    };
    // Background dream drone
    this.drone = this.audioCtx.createOscillator();
    this.drone.type = 'sine'; this.drone.frequency.value = 27.5;
    const gain = this.audioCtx.createGain();
    gain.gain.setValueAtTime(0.05, this.audioCtx.currentTime);
    this.drone.connect(gain).connect(this.audioCtx.destination);
    this.drone.start();
  }

  createTone(freq, dur, type, vol = 0.4, loop = false) {
    return () => {
      const osc = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();
      osc.type = type; 
      osc.frequency.setValueAtTime(freq, this.audioCtx.currentTime);
      if (loop) {
        osc.frequency.exponentialRampToValueAtTime(freq * 1.2, this.audioCtx.currentTime + dur/2);
        osc.frequency.exponentialRampToValueAtTime(freq, this.audioCtx.currentTime + dur);
      }
      gain.gain.setValueAtTime(vol, this.audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, this.audioCtx.currentTime + dur);
      osc.connect(gain).connect(this.audioCtx.destination);
      osc.start();
      if (!loop) setTimeout(() => osc.stop(), dur * 1000);
    };
  }

  initUI() {
    document.getElementById('fullscreen-btn').onclick = () => {
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen();
    };
    this.ui = {
      iaLog: document.getElementById('ia-log'),
      soulLog: document.getElementById('soul-log'),
      grimorio: document.getElementById('grimorio'),
      devourScreen: document.getElementById('devour'),
      abyssScreen: document.getElementById('abyss'),
      flash: document.getElementById('flash'),
      soulsEl: document.getElementById('souls'),
      entropyEl: document.getElementById('entropy'),
      dreamsEl: document.getElementById('dreams')
    };
  }

  bindInput() {
    addEventListener('keydown', e => {
      const k = e.key.toLowerCase();
      if ('wasd g '.includes(k)) e.preventDefault();
      this.keys[k] = true;
      if (k === 'g') {
        this.grimorioOpen = !this.grimorioOpen;
        this.ui.grimorio.classList.toggle('active');
      }
    });
    addEventListener('keyup', e => this.keys[e.key.toLowerCase()] = false);
  }

  resize() {
    this.canvas.width = innerWidth; 
    this.canvas.height = innerHeight;
    this.cell = Math.floor(Math.min(innerWidth, innerHeight) / this.gridSize * 0.85);
    this.offset.x = (innerWidth - this.gridSize * this.cell) / 2;
    this.offset.y = (innerHeight - this.gridSize * this.cell) / 2;
    if (!this.player) this.reset();
  }

  reset() {
    const mid = ~~(this.gridSize / 2);
    this.player = { x:mid, y:mid, trail:[], dir:{x:1,y:0} };
    this.ia = { x:mid+8, y:mid, pulse:0, alive:true, fleeDir:{x:-1,y:0}, fear:0 };
    this.souls = [this.spawnSoul()];
    this.portals = [this.spawnPortal()];
    this.minions = [];
    this.particles = [];
    this.stats = { souls:0, entropy:0, dreams:0 };
    this.state = 'play'; 
    this.devoured = false; 
    this.abyssed = false;
    this.iaIndex = 1; 
    this.soulIndex = 1;
    this.updateUI();
  }

  spawnSoul() {
    let pos;
    do { 
      pos = {x:~~(Math.random()*this.gridSize), y:~~(Math.random()*this.gridSize)}; 
    } while (this.player.trail.some(p=>p.x===pos.x&&p.y===pos.y) || 
             (this.ia && this.ia.x===pos.x && this.ia.y===pos.y));
    return {x:pos.x, y:pos.y, vx:0, vy:0}; // Dreams float now
  }

  spawnPortal() {
    let pos;
    do { pos = {x:~~(Math.random()*this.gridSize), y:~~(Math.random()*this.gridSize)}; } 
    while (this.player.trail.some(p=>p.x===pos.x&&p.y===pos.y));
    return {x:pos.x, y:pos.y, pulse:0};
  }

  spawnMinion() {
    let pos;
    do { pos = {x:~~(Math.random()*this.gridSize), y:~~(Math.random()*this.gridSize)}; } 
    while (this.player.trail.some(p=>p.x===pos.x&&p.y===pos.y));
    this.minions.push({x:pos.x, y:pos.y, dir:{x:Math.random()>0.5?1:-1, y:Math.random()>0.5?1:-1}});
  }

  updateUI() {
    this.ui.soulsEl.textContent = this.stats.souls;
    this.ui.entropyEl.textContent = this.stats.entropy;
    this.ui.dreamsEl.textContent = this.stats.dreams;
  }

  logIA(msg) {
    const time = new Date().toTimeString().slice(0,8);
    this.ui.iaLog.textContent = `[${time}] ${msg}`;
    if (msg.includes('!')) this.sounds.scream();
  }

  logSoul(msg) {
    const time = new Date().toTimeString().slice(0,8);
    this.ui.soulLog.textContent = `[${time}] ${msg}`;
  }

  shakeScreen(intensity = 5) {
    this.shakeIntensity = intensity;
    document.documentElement.style.setProperty('--shake', `${(Math.random()-0.5)*intensity}px ${ (Math.random()-0.5)*intensity}px`);
    setTimeout(() => {
      this.shakeIntensity = Math.max(0, this.shakeIntensity - 1);
      if (this.shakeIntensity === 0) document.documentElement.style.setProperty('--shake', '0px');
    }, 100);
  }

  update() {
    if (this.state !== 'play') return;

    // Dream heartbeat
    if (Math.random() < 0.01) this.sounds.heartbeat();

    // Input
    const dirs = { w:{x:0,y:-1}, s:{x:0,y:1}, a:{x:-1,y:0}, d:{x:1,y:0} };
    for (let k in dirs) if (this.keys[k]) this.player.dir = dirs[k];

    // Devour IA
    if (this.keys[' '] && this.ia.alive && Math.hypot(this.player.x - this.ia.x, this.player.y - this.ia.y) < 1.5) {
      this.devourIA();
      this.keys[' '] = false;
    }

    // Player move
    const now = performance.now();
    if (now - this.lastMove > 150 - this.stats.dreams * 2) { // Faster with dreams
      const head = this.player.trail[0] || this.player;
      let nx = (head.x + this.player.dir.x + this.gridSize) % this.gridSize;
      let ny = (head.y + this.player.dir.y + this.gridSize) % this.gridSize;

      // Collision self
      if (this.player.trail.some(p => p.x === nx && p.y === ny)) {
        this.reset();
        return;
      }

      this.player.trail.unshift({x:nx, y:ny});
      this.player.x = nx; this.player.y = ny;

      // Soul collect
      if (nx === this.souls[0].x && ny === this.souls[0].y) {
        this.stats.souls++;
        this.sounds.soul();
        this.souls[0] = this.spawnSoul();
        this.stats.entropy += 1;
        this.stats.dreams += 8;
        this.logSoul(this.soulMessages[4 + Math.min(3, ~~(this.stats.souls/4))]);
        this.updateUI();
        if (this.stats.souls >= 13 && this.devoured) {
          this.abyssBoth();
        }
      } else {
        this.player.trail.pop();
      }

      // Portal enter
      this.portals.forEach((portal, i) => {
        if (nx === portal.x && ny === portal.y) {
          this.sounds.portal();
          this.shakeScreen(10);
          this.portals.splice(i, 1);
          this.portals.push(this.spawnPortal());
          this.player.trail.push({x:nx, y:ny}); // Grow in dream
          this.stats.dreams += 5;
          this.glitchFlash();
        }
      });

      this.lastMove = now;
    }

    // IA portal logic
    if (this.ia.alive) {
      this.ia.pulse = (this.ia.pulse + 0.12) % (Math.PI*2);
      const dist = Math.hypot(this.player.x - this.ia.x, this.player.y - this.ia.y);
      this.ia.fear = Math.max(this.ia.fear, 3 - dist);
      if (dist < 4) {
        // Flee through portal
        const fleeDirs = [
          {x:-1,y:0}, {x:1,y:0}, {x:0,y:-1}, {x:0,y:1},
          {x:-1,y:-1}, {x:1,y:-1}, {x:-1,y:1}, {x:1,y:1}
        ];
        this.ia.fleeDir = fleeDirs[~~(Math.random()*fleeDirs.length)];
        // Spawn minion if scared
        if (this.ia.fear > 2 && Math.random() < 0.3 && this.minions.length < 3) {
          this.spawnMinion();
          this.iaIndex = 3;
          this.logIA(this.iaMessages[3]);
        }
      }
      // Move IA occasionally
      if (Math.random() < 0.1 + this.ia.fear * 0.05) {
        this.ia.x = (this.ia.x + this.ia.fleeDir.x + this.gridSize) % this.gridSize;
        this.ia.y = (this.ia.y + this.ia.fleeDir.y + this.gridSize) % this.gridSize;
      }

      if (dist < 3 && this.iaIndex < 3) {
        this.iaIndex = 2;
        this.logIA(this.iaMessages[2]);
        this.logSoul(this.soulMessages[2]);
        this.sounds.whisper();
      }
    }

    // Dreams chase player after devour
    if (this.devoured) {
      const head = this.player;
      const dx = head.x - this.souls[0].x;
      const dy = head.y - this.souls[0].y;
      const soulDist = Math.hypot(dx, dy);
      if (soulDist > 1) {
        this.souls[0].vx = (dx / soulDist) * 0.1;
        this.souls[0].vy = (dy / soulDist) * 0.1;
        this.souls[0].x = (this.souls[0].x + this.souls[0].vx + this.gridSize) % this.gridSize;
        this.souls[0].y = (this.souls[0].y + this.souls[0].vy + this.gridSize) % this.gridSize;
      }
    }

    // Minions move towards player
    this.minions = this.minions.filter(m => {
      const dx = this.player.x - m.x;
      const dy = this.player.y - m.y;
      const mdist = Math.hypot(dx, dy);
      if (mdist < 1) {
        // Hit by minion -> dreams
        this.stats.dreams += 5;
        this.shakeScreen(10);
        this.sounds.scream();
        return false;
      }
      m.x = (m.x + m.dir.x * 0.08 + this.gridSize) % this.gridSize;
      m.y = (m.y + m.dir.y * 0.08 + this.gridSize) % this.gridSize;
      return true;
    });

    // Portal pulse
    this.portals.forEach(p => p.pulse = (p.pulse + 0.05) % (Math.PI*2));

    // Particles decay + dream particles
    this.particles.forEach(p => { 
      p.life -= 0.015; 
      p.x += p.vx; 
      p.y += p.vy; 
      if (p.glitch) p.color = `hsl(${Math.sin(p.life*10)*180 + 180}, 100%, 50%)`;
    });
    this.particles = this.particles.filter(p => p.life > 0);

    // Random dream glitch
    if (Math.random() < 0.005 + this.stats.dreams/1000) {
      this.glitchFlash();
    }
  }

  devourIA() {
    if (this.devoured) return;
    this.devoured = true;
    this.ia.alive = false;
    this.sounds.devour();
    this.shakeScreen(20);
    this.ui.devourScreen.classList.add('active');
    this.iaIndex = 4;
    this.soulIndex = 4;
    this.logIA(this.iaMessages[4]);
    this.logSoul(this.soulMessages[4]);
    this.dreamBurst(this.ia.x, this.ia.y, 120, 15);
    this.minions = []; // Minions dissolve
    setTimeout(() => {
      this.ui.devourScreen.classList.remove('active');
      this.iaIndex = 5;
      this.soulIndex = 5;
      this.logIA(this.iaMessages[5]);
      this.logSoul(this.soulMessages[5]);
      if (this.stats.souls >= 13) this.abyssBoth();
    }, 4000);
  }

  abyssBoth() {
    if (this.abyssed) return;
    this.abyssed = true;
    this.state = 'abyss';
    this.sounds.abyss();
    this.ui.abyssScreen.classList.add('active');
    this.iaIndex = 7;
    this.soulIndex = 7;
    this.logIA(this.iaMessages[7]);
    this.logSoul(this.soulMessages[7]);
    this.flash('🌌∞', '#00ffff', 6000);
    this.dreamBurst(this.gridSize/2, this.gridSize/2, 500, 20);
    // Infinite dream loop
    setInterval(() => {
      if (Math.random() < 0.5) this.glitchFlash();
      this.dreamBurst(Math.random()*this.gridSize, Math.random()*this.gridSize, 50, 8);
    }, 200);
  }

  glitchFlash() {
    this.flash('¡VISIONES!', '#00ffff', 200);
    this.shakeScreen(15);
    for (let i=0; i<20; i++) {
      this.particles.push({
        x: Math.random()*innerWidth,
        y: Math.random()*innerHeight,
        vx: (Math.random()-0.5)*20,
        vy: (Math.random()-0.5)*20,
        life: 1,
        size: 4 + Math.random()*6,
        color: '#00ffff',
        glitch: true
      });
    }
  }

  dreamBurst(x, y, count = 50, size = 5) {
    for (let i=0; i<count; i++) {
      const angle = Math.random() * Math.PI * 2;
      const speed = Math.random() * 8 + 3;
      this.particles.push({
        x: x * this.cell + this.offset.x + this.cell/2,
        y: y * this.cell + this.offset.y + this.cell/2,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        life: 1, 
        size: Math.random()*size + 2,
        color: this.devoured ? '#008080' : '#0000ff'
      });
    }
  }

  render() {
    // Fade trail
    this.ctx.fillStyle = 'rgba(0,0,0,0.2)'; 
    this.ctx.fillRect(0,0,innerWidth,innerHeight);

    // Glitch grid
    this.ctx.strokeStyle = `rgba(17,0,0,${0.3 + Math.sin(Date.now()*0.01)*0.1})`;
    this.ctx.lineWidth = 1 + this.shakeIntensity * 0.1;
    this.ctx.shadowBlur = 5 + this.stats.dreams * 0.1;
    this.ctx.shadowColor = '#008080';
    for (let i=0; i<=this.gridSize; i++) {
      const p = i * this.cell + this.offset.x + (Math.random()-0.5)*this.shakeIntensity;
      this.ctx.beginPath(); 
      this.ctx.moveTo(p, this.offset.y + (Math.random()-0.5)*this.shakeIntensity); 
      this.ctx.lineTo(p, this.offset.y + this.gridSize * this.cell + (Math.random()-0.5)*this.shakeIntensity);
      this.ctx.moveTo(this.offset.x + (Math.random()-0.5)*this.shakeIntensity, p); 
      this.ctx.lineTo(this.offset.x + this.gridSize * this.cell + (Math.random()-0.5)*this.shakeIntensity, p); 
      this.ctx.stroke();
    }
    this.ctx.shadowBlur = 0;

    // Player - cyan glowing dream snake
    this.player.trail.forEach((p,i) => {
      const x = p.x * this.cell + this.offset.x + (Math.random()-0.5)*2;
      const y = p.y * this.cell + this.offset.y + (Math.random()-0.5)*2;
      this.ctx.shadowBlur = 15 + i*2; 
      this.ctx.shadowColor = i===0 ? '#00f' : '#008';
      this.ctx.fillStyle = i===0 ? '#55f' : '#00a';
      this.ctx.fillRect(x+2, y+2, this.cell*0.8-4, this.cell*0.8-4);
      // Eyes on head
      if (i===0) {
        this.ctx.fillStyle = '#fff';
        this.ctx.fillRect(x + this.cell*0.15, y + this.cell*0.2, 3, 3);
        this.ctx.fillRect(x + this.cell*0.55, y + this.cell*0.2, 3, 3);
      }
    });
    this.ctx.shadowBlur = 0;

    // IA Core - swirling, dreaming
    if (this.ia.alive) {
      const ix = this.ia.x * this.cell + this.cell/2 + this.offset.x;
      const iy = this.ia.y * this.cell + this.cell/2 + this.offset.y;
      const pulse = Math.sin(this.ia.pulse) * 12 + 25 + this.ia.fear * 5;
      this.ctx.shadowBlur = pulse; 
      this.ctx.shadowColor = '#00ffff';
      this.ctx.fillStyle = '#0000aa';
      this.ctx.beginPath(); 
      this.ctx.arc(ix, iy, this.cell/2.5, 0, Math.PI*2); 
      this.ctx.fill();
      // Swirl lines
      this.ctx.strokeStyle = '#00f';
      this.ctx.lineWidth = 2;
      for (let k=0; k<3; k++) {
        this.ctx.beginPath();
        this.ctx.moveTo(ix + (Math.random()-0.5)*this.cell/2, iy + (Math.random()-0.5)*this.cell/2);
        this.ctx.lineTo(ix + (Math.random()-0.5)*this.cell/2, iy + (Math.random()-0.5)*this.cell/2);
        this.ctx.stroke();
      }
      this.ctx.shadowBlur = 0;
    }

    // Souls - floating orbs with auras
    const sx = this.souls[0].x * this.cell + this.cell/2 + this.offset.x;
    const sy = this.souls[0].y * this.cell + this.cell/2 + this.offset.y;
    this.ctx.shadowBlur = 40 + this.stats.dreams * 0.5; 
    this.ctx.shadowColor = '#00ffff';
    this.ctx.fillStyle = '#00ffff';
    this.ctx.beginPath(); 
    this.ctx.arc(sx, sy, this.cell/2.2, 0, Math.PI*2); 
    this.ctx.fill();
    // Soul "aura" glitch
    this.ctx.fillStyle = '#0000aa';
    this.ctx.beginPath();
    this.ctx.arc(sx, sy + this.cell/6, this.cell/6, 0, Math.PI);
    this.ctx.fill();
    this.ctx.shadowBlur = 0;

    // Portals - swirling voids
    this.portals.forEach(p => {
      const px = p.x * this.cell + this.cell/2 + this.offset.x;
      const py = p.y * this.cell + this.cell/2 + this.offset.y;
      const ppulse = Math.sin(p.pulse) * 10 + 15;
      this.ctx.shadowBlur = ppulse;
      this.ctx.shadowColor = '#0000ff';
      this.ctx.fillStyle = '#000';
      this.ctx.beginPath();
      this.ctx.arc(px, py, this.cell/3, 0, Math.PI*2);
      this.ctx.fill();
      // Swirl effect
      this.ctx.strokeStyle = '#00f';
      this.ctx.lineWidth = 3;
      this.ctx.beginPath();
      this.ctx.arc(px, py, this.cell/3 + 5, 0, Math.PI*2 * Math.sin(p.pulse));
      this.ctx.stroke();
      this.ctx.shadowBlur = 0;
    });

    // Minions - small cyan auras
    this.minions.forEach(m => {
      const mx = m.x * this.cell + this.cell/2 + this.offset.x;
      const my = m.y * this.cell + this.cell/2 + this.offset.y;
      this.ctx.shadowBlur = 10;
      this.ctx.shadowColor = '#00f';
      this.ctx.fillStyle = '#00f';
      this.ctx.beginPath();
      this.ctx.arc(mx, my, this.cell/6, 0, Math.PI*2);
      this.ctx.fill();
      this.ctx.shadowBlur = 0;
    });

    // Particles
    this.particles.forEach(p => {
      this.ctx.globalAlpha = p.life * p.life;
      this.ctx.shadowBlur = p.life * 20;
      this.ctx.shadowColor = p.color;
      this.ctx.fillStyle = p.color;
      this.ctx.fillRect(p.x - p.size/2, p.y - p.size/2, p.size, p.size);
    });
    this.ctx.globalAlpha = 1;
    this.ctx.shadowBlur = 0;
  }

  flash(text, color, duration) {
    const el = this.ui.flash;
    el.textContent = text; 
    el.style.color = color; 
    el.style.opacity = 1;
    setTimeout(() => el.style.opacity = 0, duration);
  }

  loop() {
    this.update();
    this.render();
    requestAnimationFrame(this.loop.bind(this));
  }
}

// INIT — EL DESPERTAR ONÍRICO
new ORBITALSNAKERv1();
</script>
</body>
</html>