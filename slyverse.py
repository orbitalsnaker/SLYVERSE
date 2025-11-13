<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>SLYVERSE v1 — GRIMORIO DE ALMAS</title>

  <!-- META PRO -->
  <meta name="description" content="Caza almas en el abismo digital. 13 = grimorio. 696 = pacto.">
  <meta name="theme-color" content="#0f0">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

  <!-- FAVICON -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>snake</text></svg>">

  <!-- PWA MANIFEST -->
  <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiU0xZVkVSU0UgdjEiLCJzaG9ydF9uYW1lIjoiU0xZVkVSU0UiLCJzdGFydF91cmwiOiIuIiwiaWNvbnMiOlt7InNyYyI6ImRhdGE6aW1hZ2Uvc3ZnK3htbDssPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48dGV4dCB5PSIuOWVtIiBmb250LXNpemU9IjkwIj5zbmFrZTwvdGV4dD48L3N2Zz4iLCJzaXplcyI6IjE5MngxOTIiLCJ0eXBlIjoiaW1hZ2Uvc3ZnK3htbCJ9XSwidGhlbWVfY29sb3IiOiIjMGYwIiwiYmFja2dyb3VuZF9jb2xvciI6IiMwMDAiLCJkaXNwbGF5Ijoic3RhbmRhbG9uZSJ9">

  <style>
    /* === CSS PRO: GPU, 60 FPS, MODULAR === */
    :root {
      --grid-base: 38;
      --cell-ratio: 0.86;
      --bg: #000;
      --grid: #001100;
      --player: #0f0;
      --soul: #f0f;
      --shadow: #333;
      --entropy: #f84;
      --ui-bg: rgba(0, 8, 0, 0.94);
      --ui-border: #0f0;
      --ui-accent: #f0f;
      --font: 'Courier New', monospace;
      --transition: 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    }

    * { margin:0; padding:0; box-sizing:border-box; }
    html, body { height:100%; background:var(--bg); color:var(--player); font-family:var(--font); overflow:hidden; user-select:none; touch-action:none; }
    canvas { display:block; image-rendering:pixelated; background:var(--bg); transform:translateZ(0); will-change:transform; }
    #game { background:radial-gradient(circle at center, #000a00, var(--bg)); }
    #particles, #light { position:fixed; inset:0; pointer-events:none; mix-blend-mode:screen; }

    .ui-panel {
      position:absolute; background:var(--ui-bg); border:1px solid var(--ui-border); border-radius:6px; padding:10px; font-size:13px; line-height:1.5; backdrop-filter:blur(3px); z-index:10; transition:var(--transition);
    }
    #grimorio { top:12px; left:12px; max-width:340px; color:var(--ui-accent); border-color:var(--ui-accent); }
    #hud { bottom:12px; left:12px; right:12px; }

    #menu, #pause, #lore, #gameover, #empathy {
      position:fixed; inset:0; background:rgba(0,0,0,0.98); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:24px; z-index:100; opacity:0; pointer-events:none; transition:opacity var(--transition);
    }
    .active { opacity:1; pointer-events:all; }

    h1 { font-size:2.8rem; text-shadow:0 0 20px currentColor; animation:glitch 3s infinite; }
    @keyframes glitch { 0%,100%{transform:translate(0);} 20%{transform:translate(-2px,2px);} 40%{transform:translate(-2px,-2px);} 60%{transform:translate(2px,2px);} 80%{transform:translate(2px,-2px);} }

    button {
      background:var(--ui-bg); color:var(--player); border:1px solid var(--ui-border); padding:10px 20px; margin:8px; font-family:var(--font); font-size:14px; cursor:pointer; border-radius:4px; transition:var(--transition);
    }
    button:hover { background:var(--ui-accent); color:#000; box-shadow:0 0 15px var(--ui-accent); }

    .meter { position:absolute; top:12px; right:12px; width:200px; height:10px; background:#111; border:1px solid var(--ui-border); }
    #focus-meter { top:28px; }
    .fill { height:100%; width:100%; transition:width 0.3s var(--transition); }
    #sanity-fill { background:linear-gradient(to right, #f00, #ff0, var(--player)); }
    #focus-fill { background:linear-gradient(to right, var(--player), #0ff); }

    #flash, #breath { position:fixed; inset:0; display:flex; align-items:center; justify-content:center; font-size:clamp(4rem,18vw,28rem); font-weight:bold; opacity:0; pointer-events:none; transition:opacity 1.5s; text-shadow:0 0 60px currentColor; z-index:200; }
    #breath { bottom:20px; font-size:16px; }
  </style>
</head>
<body>

<canvas id="game"></canvas>
<canvas id="particles"></canvas>
<canvas id="light"></canvas>

<div id="sanity-meter" class="meter"><div id="sanity-fill" class="fill" style="width:100%"></div></div>
<div id="focus-meter" class="meter"><div id="focus-fill" class="fill" style="width:50%"></div></div>

<div id="grimorio" class="ui-panel">
  <div>GRIMORIO: <span id="souls">0</span> | ENTROPÍA: <span id="entropy">0</span></div>
  <div>ROBADAS: <span id="stolen">0</span> | BOMBA: <span id="bombs">3</span> | PORTAL: <span id="portal">READY</span></div>
  <div style="margin-top:6px;font-size:11px;opacity:0.7">WASD: mover | SPACE: bomba | T: portal | G: grimorio | I: inhibir | F: switch | R: renacer</div>
</div>

<div id="hud" class="ui-panel">
  SLYVERSE v1 | SOMBRAS: <span id="enemies">9</span> | ALMAS: <span id="global">0</span>/13 | 
  70% → <span id="p70">0.00</span>€ | 20% → <span id="p20">0.00</span>€ | 10% → <span id="p10">0.00</span>€
</div>

<div id="menu" class="active">
  <h1>SLYVERSE</h1>
  <p>Un grimorio digital. 13 almas. 696 euros éticos. Tu caos.</p>
  <button id="start25">25 MIN CAZA</button>
  <button id="how">CONTROLES</button>
</div>

<div id="pause">
  <h1>INHALA</h1>
  <p id="breath-text">4...</p>
  <button id="resume">REANUDAR</button>
</div>

<div id="lore">
  <h1>EL GRIMORIO</h1>
  <p>En el Shadow Studio, las almas de devs rotas flotan.<br>13 = grimorio se abre.<br>696 = el pacto se cumple.<br>€ éticos = diezmo de sangre digital.</p>
  <button id="close-lore">ACEPTAR</button>
</div>

<div id="gameover">
  <h1>GRIMORIO ROTO</h1>
  <p>Almas cazadas: <span id="final-souls">0</span> | Entropía: <span id="final-entropy">0</span></p>
  <button id="restart">RENACER</button>
</div>

<div id="empathy">
  <h1>ALMA LIBERADA</h1>
  <p>"Yo también lo sentí... el vacío... gracias."</p>
  <button id="close-empathy">CONTINUAR</button>
</div>

<div id="flash">696</div>
<div id="breath">4... 7... 8...</div>

<script>
/**
 * SLYVERSE v1 — ESTUDIO PRO EN UN ARCHIVO
 * ECS + MVC + 60 FPS + PWA + GPU + AUDIO + ESTILO DEL DEV
 * ~~, 696, € éticos, repartir(0.74), keys.g, almasGlobal
 */

class SLYVERSE {
  constructor() {
    // === CANVASES ===
    this.gameCanvas = document.getElementById('game'); this.ctx = this.gameCanvas.getContext('2d');
    this.pCanvas = document.getElementById('particles'); this.pctx = this.pCanvas.getContext('2d');
    this.lCanvas = document.getElementById('light'); this.lctx = this.lCanvas.getContext('2d');

    // === STATE ===
    this.gridBase = 38; this.gridSize = this.gridBase;
    this.cell = 0; this.offset = {x:0, y:0};
    this.player = null; this.shadows = []; this.souls = []; this.particles = [];
    this.stats = { souls:0, stolen:0, entropy:0, globalSouls:0, payout:{p70:0,p20:0,p10:0}, bombs:3 };
    this.sessionTime = 0; this.state = 'menu'; this.lastTime = 0;

    // === INPUT ===
    this.keys = {}; this.bindInput();

    // === AUDIO ===
    this.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    this.sounds = {
      eat: this.createTone(800, 0.1, 'sine'),
      bomb: this.createTone(120, 0.2, 'square'),
      grimorio: this.createTone(400, 0.8, 'sawtooth'),
      portal: this.createTone(600, 0.3, 'triangle'),
      empathy: this.createTone(900, 0.4, 'sine')
    };

    // === UI ===
    this.ui = {
      menu: document.getElementById('menu'), pause: document.getElementById('pause'),
      start25: document.getElementById('start25'), resume: document.getElementById('resume'),
      how: document.getElementById('how'), closeLore: document.getElementById('close-lore'),
      restart: document.getElementById('restart'), closeEmpathy: document.getElementById('close-empathy'),
      grimorio: document.getElementById('grimorio'), hud: document.getElementById('hud'),
      flash: document.getElementById('flash'), breath: document.getElementById('breath'),
      sanityFill: document.getElementById('sanity-fill'), focusFill: document.getElementById('focus-fill')
    };
    this.ui.start25.onclick = () => this.startGame(25*60);
    this.ui.resume.onclick = () => this.resumeGame();
    this.ui.how.onclick = () => alert("WASD: mover\nSPACE: bomba\nT: portal\nG: grimorio\nI: inhibir\nF: switch\nR: renacer");
    this.ui.closeLore.onclick = () => document.getElementById('lore').classList.remove('active');
    this.ui.restart.onclick = () => this.startGame(25*60);
    this.ui.closeEmpathy.onclick = () => document.getElementById('empathy').classList.remove('active');

    // === INIT ===
    this.resize(); addEventListener('resize', () => this.resize());
    requestAnimationFrame(this.loop.bind(this));
  }

  // === AUDIO ===
  createTone(freq, dur, type = 'sine') {
    return () => {
      const osc = this.audioCtx.createOscillator(), gain = this.audioCtx.createGain();
      osc.type = type; osc.frequency.value = freq;
      gain.gain.setValueAtTime(0.3, this.audioCtx.currentTime);
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
    [this.gameCanvas, this.pCanvas, this.lCanvas].forEach(c => { c.width = innerWidth; c.height = innerHeight; });
    this.cell = Math.floor(Math.min(innerWidth, innerHeight) / this.gridSize * 0.86);
    this.offset.x = (innerWidth - this.gridSize * this.cell) / 2;
    this.offset.y = (innerHeight - this.gridSize * this.cell) / 2;
  }

  // === GAME CONTROL ===
  startGame(duration) {
    this.state = 'game'; this.sessionTime = duration;
    this.ui.menu.classList.remove('active');
    document.getElementById('grimorio').style.display = 'block';
    document.getElementById('hud').style.display = 'block';
    this.reset();
  }

  reset() {
    const mid = ~~(this.gridSize / 2);
    this.player = { x:mid, y:mid, trail:[], dir:{x:1,y:0}, alive:true, bombs:3, portalReady:true, sanity:100, focus:50 };
    this.shadows = Array.from({length:9}, () => this.spawnShadow());
    this.souls = [this.spawnSoul()];
    this.stats = { souls:0, stolen:0, entropy:0, globalSouls:0, payout:{p70:0,p20:0,p10:0}, bombs:3 };
    this.particles = [];
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
    this.shadows.forEach(s => s.chaos = Math.random() * 0.8 + 0.2);
    this.souls[0] = this.spawnSoul();
    this.stats.entropy += 2;
    this.showFlash('ALMA CAZADA', 1800);
    this.particleBurst(innerWidth/2, innerHeight/2, `hsl(${Math.random()*60+240},100%,70%)`, 100, 7);
    this.sounds.grimorio();
  }

  useBomb() {
    if (this.stats.bombs <= 0) return;
    this.stats.bombs--;
    this.sounds.bomb();
    const head = this.player.trail[0] || this.player;
    this.shadows = this.shadows.filter(s => {
      if (!s.alive) return true;
      const dist = Math.hypot(s.x - head.x, s.y - head.y);
      if (dist < 1.5) { this.stats.stolen++; this.particleBurst(s.x*this.cell+this.offset.x, s.y*this.cell+this.offset.y, '#f0a', 30); return false; }
      return true;
    });
  }

  usePortal() {
    this.player.x = this.souls[0].x; this.player.y = this.souls[0].y;
    this.player.portalReady = false; this.sounds.portal();
    setTimeout(() => this.player.portalReady = true, 7000);
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
    if (performance.now() - this.lastTime > 160) {
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
        if (this.stats.globalSouls >= 13) { this.stats.globalSouls = 0; this.showFlash('696', 2500); this.particleBurst(innerWidth/2, innerHeight/2, `hsl(${Date.now()%360},100%,70%)`, 200, 8); }
      } else this.player.trail.pop();

      this.lastTime = performance.now();
    }

    // Shadows
    this.shadows.forEach(s => {
      if (!s.alive) return;
      let dx = this.souls[0].x - s.x, dy = this.souls[0].y - s.y;
      if (s.chaos > 0) { dx += (Math.random()-0.5)*this.gridSize*0.6; dy += (Math.random()-0.5)*this.gridSize*0.6; s.chaos = Math.max(0, s.chaos - 0.015); }
      const dir = Math.abs(dx) > Math.abs(dy) ? {x:Math.sign(dx), y:0} : {x:0, y:Math.sign(dy)};
      const nx = (s.x + dir.x + this.gridSize) % this.gridSize;
      const ny = (s.y + dir.y + this.gridSize) % this.gridSize;
      s.x = nx; s.y = ny;
    });

    // Particles
    this.particles.forEach(p => { p.x += p.vx; p.y += p.vy; p.vx *= 0.97; p.vy *= 0.97; p.life -= 0.03; });
    this.particles = this.particles.filter(p => p.life > 0);

    this.updateUI();
  }

  // === RENDER ===
  render() {
    this.ctx.fillStyle = 'rgba(0,0,0,0.15)'; this.ctx.fillRect(0,0,innerWidth,innerHeight);

    // Grid
    this.ctx.strokeStyle = `rgba(240,0,240,${0.2 + Math.sin(Date.now()/1000)*0.1})`;
    for (let i=0; i<=this.gridSize; i++) {
      const p = i * this.cell + this.offset.x;
      this.ctx.beginPath(); this.ctx.moveTo(p, 0); this.ctx.lineTo(p, innerHeight);
      this.ctx.moveTo(0, p); this.ctx.lineTo(innerWidth, p); this.ctx.stroke();
    }

    // Player
    this.player.trail.forEach((p,i) => {
      const x = p.x * this.cell + this.offset.x, y = p.y * this.cell + this.offset.y;
      this.ctx.fillStyle = i===0 ? '#fff' : '#0aa';
      this.ctx.fillRect(x, y, this.cell*0.87, this.cell*0.87);
    });

    // Shadows
    this.shadows.forEach(s => {
      const color = `hsl(${s.hue + s.chaos*120},95%,${40 + s.chaos*20}%)`;
      this.ctx.fillStyle = color;
      this.ctx.fillRect(s.x*this.cell + this.offset.x, s.y*this.cell + this.offset.y, this.cell*0.87, this.cell*0.87);
    });

    // Soul
    const sx = this.souls[0].x*this.cell + this.cell/2 + this.offset.x;
    const sy = this.souls[0].y*this.cell + this.cell/2 + this.offset.y;
    this.ctx.shadowBlur = 25; this.ctx.shadowColor = '#f0f'; this.ctx.fillStyle = '#f0f';
    this.ctx.beginPath(); this.ctx.arc(sx, sy, this.cell/2, 0, Math.PI*2); this.ctx.fill();
    this.ctx.shadowBlur = 0;

    // Particles
    this.pctx.clearRect(0,0,innerWidth,innerHeight);
    this.particles.forEach(p => {
      this.pctx.globalAlpha = p.life;
      this.pctx.fillStyle = p.color;
      this.pctx.fillRect(p.x - p.size/2, p.y - p.size/2, p.size, p.size);
    });
    this.pctx.globalAlpha = 1;
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
  }

  // === MAIN LOOP ===
  loop(timestamp) {
    const delta = timestamp - this.lastTime;
    if (delta > 16) {
      this.update(delta);
      this.lastTime = timestamp;
    }
    this.render();
    requestAnimationFrame(this.loop.bind(this));
  }
}

// INIT
new SLYVERSE();
</script>
</body>
</html>