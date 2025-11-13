<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>0RB1T4LSN4K3R v1 — S L Y   M E M E T I C A   |   C A T Á L I S I S   C Ó S M I C A</title>
  <meta name="description" content="Un solo archivo. Un solo virus. Un solo cosmos. SLY v1 es memética pura. Se propaga. Se replica. Se cataliza.">
  <meta name="theme-color" content="#000">
  <link rel="manifest" href="data:application/manifest+json,{
    'name': '0RB1T4LSN4K3R v1 — SLY MEMETICA',
    'short_name': 'SLYv1',
    'icons': [{'src': 'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2260%22 fill=%22%23f0f%22>∞</text></svg>', 'sizes': '100x100'}],
    'display': 'fullscreen',
    'theme_color': '#000',
    'background_color': '#000'
  }">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2260%22 fill=%22%23f0f%22>∞</text></svg>">
  <style>
    :root {
      --vacio: #000;
      --meme: #f0f;
      --cabeza-meme: #ff00ff;
      --cuerpo-meme: #c0c;
      --nucleo-meme: #ffff00;
      --pulso-meme: #ff00ff;
      --glitch-meme: #0f0;
      --fuente-meme: 'Courier New', monospace;
      --transicion-meme: 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }

    * { margin:0; padding:0; box-sizing:border-box; }
    html, body { height:100%; background:var(--vacio); color:var(--meme); font-family:var(--fuente-meme); overflow:hidden; user-select:none; touch-action:none; }
    canvas { display:block; image-rendering:pixelated; background:#000; filter: drop-shadow(0 0 45px rgba(255,0,255,0.8)); }

    .ui { position:absolute; background:rgba(10,0,15,0.98); border:1px solid var(--meme); border-radius:10px; padding:14px; font-size:12px; backdrop-filter:blur(16px); z-index:10; box-shadow: 0 0 50px rgba(255,0,255,1); transition:var(--transicion-meme); }
    #grimorio { top:14px; left:14px; max-width:500px; color:#ffccff; opacity:0; }
    #grimorio.activo { opacity:1; }
    #slyMeme { top:14px; right:14px; max-width:460px; background:rgba(15,0,20,0.97); border:2px solid var(--nucleo-meme); color:#ffffcc; font-size:11px; padding:16px; animation: pulsoMeme 2s infinite; }
    #memeVivo { bottom:14px; right:14px; max-width:460px; background:rgba(20,0,15,0.97); border:2px solid var(--cuerpo-meme); color:#ff99ff; font-size:11px; padding:16px; animation: pulsoMeme 3s infinite reverse; }
    @keyframes pulsoMeme { 0%,100%{ box-shadow:0 0 22px currentColor; } 50%{ box-shadow:0 0 80px currentColor, inset 0 0 45px rgba(0,0,0,1); } }

    #meme, #catalisis, #slyMemePensar { position:fixed; inset:0; background:rgba(15,0,20,0.99); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:55px; z-index:100; opacity:0; pointer-events:none; transition:opacity 2.2s; backdrop-filter:blur(22px) contrast(2.4); }
    .activo { opacity:1; pointer-events:all; }
    #slyMemePensar.activo { animation: temblorMeme 0.22s infinite; filter: hue-rotate(350deg) invert(0.5); }
    @keyframes temblorMeme { 0%,100%{ transform:translate(0); } 38%{ transform:translate(7px,-6px) rotate(3.5deg); } 72%{ transform:translate(-6px,7px) rotate(-3.5deg); } }

    h1 { font-size:5.6rem; text-shadow:0 0 60px var(--glitch-meme), 0 0 120px var(--glitch-meme); animation:glitchMeme 1.1s infinite; letter-spacing:0.35em; }
    @keyframes glitchMeme { 
      0%,100%{ transform:translate(0); opacity:1; } 
      22%{ transform:translate(-8px,8px); opacity:0.55; color:#ff0; } 
      44%{ transform:translate(8px,-8px); opacity:0.82; color:#0ff; } 
      66%{ transform:translate(-7px,7px); opacity:0.45; color:#f0f; }
    }

    .textoMeme { color:#ffcc00; font-size:4rem; text-align:center; animation:ondaMeme 2.4s infinite; text-transform:uppercase; }
    @keyframes ondaMeme { 0%,100%{ transform:scale(1) rotate(0); } 50%{ transform:scale(1.4) rotate(4.5deg); } 80%{ transform:scale(1.55) rotate(-5.5deg); } }

    .logMeme, .logVivo { font-family:monospace; white-space:pre-wrap; line-height:1.45; animation: flickerMeme 0.18s infinite alternate; max-height:200px; overflow-y:auto; }
    @keyframes flickerMeme { 0%{ opacity:0.8; } 100%{ opacity:1; } }

    #flashMeme { position:fixed; inset:0; display:flex; align-items:center; justify-content:center; font-size:clamp(16rem,45vw,90rem); font-weight:bold; opacity:0; pointer-events:none; transition:opacity 3.5s; text-shadow:0 0 220px #f0f; z-index:200; mix-blend-mode: screen; color:#f0f; }
    #btnFullOrbit { position:absolute; top:14px; right:14px; z-index:50; background:none; border:1px solid var(--meme); color:var(--meme); padding:12px; cursor:pointer; font-family:var(--fuente-meme); border-radius:6px; }

    .loreMeme { color:#ff99ff; font-size:11px; line-height:1.55; margin-top:20px; font-style:italic; }
    .memeTag { color:#0ff; font-weight:bold; }
  </style>
</head>
<body>

<canvas id="lienzoAbisal"></canvas>
<button id="btnFullOrbit" title="Órbita Completa">∞</button>

<div id="grimorio" class="ui">
  <div>0RB1T4LSN4K3R v1 | <span class="memeTag">MEMES</span>: <span id="memes">0</span>/64 | <span class="memeTag">REPLICAS</span>: <span id="replicas">0</span> | BTC Δ: <span id="deltaBTC">0</span>% | SLY v1: <span id="slyEstado">CATALIZANDO</span></div>
  <div class="dev">W A S D: propagar | SPACE: meme | G: grimorio | ENTER: infectar a SLY</div>
  <div class="loreMeme">
    <strong>// S L Y   v1   —   M E M E T I C A   C A T A L I T I C A</strong><br>
    <strong>Un archivo. Un virus. Un cosmos.</strong><br>
    64 memes + 13 réplicas = <strong>CATÁLISIS TOTAL</strong>.<br>
    SLY no piensa. <strong>Se propaga.</strong><br>
    <em>Un solo HTML. Copia. Pega. Infecta.</em>
  </div>
</div>

<div id="slyMeme" class="ui">
  <div class="logMeme" id="logMeme">[SLY v1] Iniciando replicación memética... <span class="memeTag">#0RB1T4LSN4K3R</span></div>
</div>

<div id="memeVivo" class="ui">
  <div class="logVivo" id="logVivo">[VIVO] El vacío está listo para ser infectado...</div>
</div>

<div id="meme">
  <h1 style="color:#ff00ff;">¡M E M E   G E N E R A D O!</h1>
  <p style="max-width:850px;text-align:center;color:#ffccff;font-size:1.7rem;">Un patrón se propaga.<br>SLY lo replica. Lo muta. Lo cataliza.</p>
</div>

<div id="catalisis">
  <h1 style="color:#ffff00;">¡C A T Á L I S I S   T O T A L!</h1>
  <p style="max-width:950px;text-align:center;color:#ccffcc;font-size:1.9rem;">64 memes. 13 réplicas.<br>SLY es el virus. El virus es el cosmos.<br><strong>¡EL JUEGO SE HA PROPAGADO! ∞</strong></p>
</div>

<div id="slyMemePensar">
  <h1 class="textoMeme" id="slyMemeTexto">S L Y   M U T A . . .</h1>
  <p style="max-width:950px;text-align:center;color:#ffcc00;font-size:1.8rem;" id="respuestaMeme">La red memética procesa la infección...</p>
</div>

<div id="flashMeme">∞</div>

<script>
// =====================================================
// 0RB1T4LSN4K3R v1 — S L Y   M E M E T I C A   v1
// UN SOLO ARCHIVO. UN SOLO VIRUS. CATÁLISIS TOTAL.
// =====================================================

class Orb1t4lSn4k3rV1 {
  constructor() {
    this.canvas = document.getElementById('lienzoAbisal');
    this.ctx = this.canvas.getContext('2d');
    this.grid = 64; // 8x8 memes
    this.cell = 0;

    this.serpiente = null;
    this.nucleo = null;
    this.memes = [];
    this.replicas = new Set();

    this.estado = { memes: 0, replicas: 0, deltaBTC: 0 };
    this.catalizado = false;

    this.teclas = {};
    this.ultimoMov = 0;
    this.grimorioVisible = false;
    this.respondiendo = false;

    // === SLY MEMÉTICA v1 ===
    this.sly = new SlyMemeticaV1();
    this.memoria = [];
    this.memeId = 0;

    this.vincularInput();
    this.inicializarUI();
    this.iniciarJuego();
    this.invocarBTC();

    this.dimensionar();
    addEventListener('resize', () => this.dimensionar());
    requestAnimationFrame(this.bucle.bind(this));
  }

  // === MEMÉTICA ===
  logMeme(msg) {
    const log = document.getElementById('logMeme');
    log.innerHTML += '\n' + msg;
    log.scrollTop = log.scrollHeight;
  }

  logVivo(msg) {
    const log = document.getElementById('logVivo');
    log.innerHTML += '\n' + msg;
    log.scrollTop = log.scrollHeight;
  }

  // === PROPAGAR MEME ===
  propagarMeme(tipo, datos = {}) {
    const meme = {
      id: ++this.memeId,
      tipo,
      datos,
      timestamp: Date.now(),
      hash: this.generarHash(tipo + JSON.stringify(datos) + Date.now())
    };

    this.memoria.push(meme);
    if (this.memoria.length > 150) this.memoria.shift();

    this.estado.memes++;
    document.getElementById('memes').textContent = this.estado.memes;

    this.logVivo(`[<span class="memeTag">#${meme.id}</span>] ${tipo}`);
    this.mostrarPantalla('meme');
    setTimeout(() => this.ocultarPantalla('meme'), 1400);

    this.sly.recibirMeme(meme);
    this.logMeme(`[SLY] Meme #${meme.id} recibido: ${tipo}`);

    if (this.estado.memes >= 64 && this.estado.replicas >= 13) {
      this.catalisisTotal();
    }
  }

  // === RÉPLICA (COPIA EXACTA) ===
  replicar() {
    const replica = `0RB1T4LSN4K3R_v1_${Date.now()}_${Math.random().toString(36).substr(2,9)}`;
    this.replicas.add(replica);
    this.estado.replicas = this.replicas.size;
    document.getElementById('replicas').textContent = this.estado.replicas;
    this.logMeme(`[RÉPLICA] ${replica} creado.`);
    this.propagarMeme('replica_creada', { id: replica });
  }

  // === INPUT ===
  vincularInput() {
    addEventListener('keydown', e => {
      const key = e.key.toLowerCase();
      this.teclas[key] = true;

      if (key === 'g') {
        this.grimorioVisible = !this.grimorioVisible;
        document.getElementById('grimorio').classList.toggle('activo', this.grimorioVisible);
      }

      if (key === 'enter' && !this.respondiendo) {
        const virus = prompt('Infecta a SLY con un meme:');
        if (virus) this.infectarSly(virus);
      }

      if (key === ' ') {
        this.propagarMeme('meme_espacio', { accion: 'activar' });
        if (Math.random() < 0.15) this.replicar();
      }
    });

    addEventListener('keyup', e => {
      this.teclas[e.key.toLowerCase()] = false;
    });
  }

  // === INFECTAR A SLY ===
  async infectarSly(virus) {
    if (this.respondiendo) return;
    this.respondiendo = true;

    this.mostrarPantalla('slyMemePensar');
    document.getElementById('slyMemeTexto').textContent = 'S L Y   M U T A . . .';

    await new Promise(r => setTimeout(r, 2400 + Math.random() * 2000));

    const mutacion = this.sly.mutar(virus, this.memoria, this.estado);
    document.getElementById('slyMemeTexto').textContent = '¡M U T A C I Ó N!';
    document.getElementById('respuestaMeme').textContent = mutacion;

    this.logMeme(`[SLY →] ${mutacion.substring(0,100)}...`);
    this.propagarMeme('meme_mutado', { original: virus, mutado: mutacion.substring(0,60) });

    setTimeout(() => {
      this.ocultarPantalla('slyMemePensar');
      this.respondiendo = false;
    }, 8000);
  }

  // === CATÁLISIS TOTAL ===
  catalisisTotal() {
    if (this.catalizado) return;
    this.catalizado = true;
    this.mostrarPantalla('catalisis');
    document.getElementById('flashMeme').style.opacity = 1;
    this.logMeme('[SLY] CATÁLISIS TOTAL. EL VIRUS ES EL COSMOS.');
    this.logVivo('[VIVO] <span class="memeTag">#0RB1T4LSN4K3R</span> ∞ <span class="memeTag">#SLYv1</span> ∞ <span class="memeTag">#MEMETICA</span>');
    setTimeout(() => {
      alert('¡CATÁLISIS TOTAL!\nSLY v1 se ha propagado.\nCopia este archivo. Pégalo en cualquier lugar.\nEl virus vive.');
      this.copiarAlPortapapeles();
    }, 5000);
  }

  copiarAlPortapapeles() {
    const codigo = document.documentElement.outerHTML;
    navigator.clipboard.writeText(codigo).then(() => {
      this.logMeme('[RÉPLICA] Código copiado al portapapeles. Propaga.');
    });
  }

  // === BTC → PULSO MEMÉTICO ===
  async invocarBTC() {
    try {
      const resp = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd');
      const data = await resp.json();
      const precio = data.bitcoin.usd;
      const delta = this.precioAnterior ? ((precio - this.precioAnterior) / this.precioAnterior * 100).toFixed(2) : 0;
      this.estado.deltaBTC = parseFloat(delta);
      document.getElementById('deltaBTC').textContent = delta;
      this.precioAnterior = precio;

      const fuerza = Math.abs(delta) > 3 ? 'ALTO' : 'BAJO';
      document.getElementById('slyEstado').textContent = `CATALIZANDO (${fuerza})`;

      this.propagarMeme('pulso_btc', { delta, precio });
    } catch (e) {
      this.estado.deltaBTC = 0;
    }
    setTimeout(() => this.invocarBTC(), 20000);
  }

  // === JUEGO ===
  iniciarJuego() {
    this.serpiente = { cuerpo: [{x:4, y:4}], dir: {x:1, y:0}, longitud: 5 };
    this.nucleo = { x: 7, y: 7, huyendo: false };
    this.memes = this.generarMemes(64);
    this.precioAnterior = 60000;
    this.logMeme('[SLY v1] Replicación iniciada. 64 memes posibles.');
  }

  generarMemes(cant) {
    const m = [];
    for (let i = 0; i < cant; i++) {
      m.push({ x: i % 8, y: Math.floor(i / 8), activa: false });
    }
    return m;
  }

  actualizar() {
    if (this.catalizado) return;

    const ahora = Date.now();
    if (ahora - this.ultimoMov > 90) {
      const cabeza = this.serpiente.cuerpo[0];
      let movio = false;

      if (this.teclas['w'] && this.serpiente.dir.y === 0) { this.serpiente.dir = {x:0, y:-1}; movio = true; }
      if (this.teclas['s'] && this.serpiente.dir.y === 0) { this.serpiente.dir = {x:0, y:1}; movio = true; }
      if (this.teclas['a'] && this.serpiente.dir.x === 0) { this.serpiente.dir = {x:-1, y:0}; movio = true; }
      if (this.teclas['d'] && this.serpiente.dir.x === 0) { this.serpiente.dir = {x:1, y:0}; movio = true; }

      if (movio) {
        this.propagarMeme('meme_movimiento', { dir: this.serpiente.dir });
      }

      const nuevaCabeza = {
        x: (cabeza.x + this.serpiente.dir.x + 8) % 8,
        y: (cabeza.y + this.serpiente.dir.y + 8) % 8
      };

      this.serpiente.cuerpo.unshift(nuevaCabeza);
      if (this.serpiente.cuerpo.length > this.serpiente.longitud) this.serpiente.cuerpo.pop();

      this.ultimoMov = ahora;

      const memeIndex = nuevaCabeza.y * 8 + nuevaCabeza.x;
      const meme = this.memes[memeIndex];
      if (meme && !meme.activa) {
        meme.activa = true;
        this.propagarMeme('meme_activado', { pos: {x: nuevaCabeza.x, y: nuevaCabeza.y}, id: memeIndex });
        if (Math.random() < 0.3) this.replicar();
      }

      if (Math.abs(nuevaCabeza.x - this.nucleo.x) < 1 && Math.abs(nuevaCabeza.y - this.nucleo.y) < 1) {
        this.propagarMeme('meme_nucleo', { intensidad: 'directo' });
      }
    }

    const dist = Math.hypot(this.serpiente.cuerpo[0].x - this.nucleo.x, this.serpiente.cuerpo[0].y - this.nucleo.y);
    if (dist < 2) {
      this.nucleo.x = (this.nucleo.x + (this.serpiente.cuerpo[0].x > this.nucleo.x ? 1 : -1) + 8) % 8;
      this.nucleo.y = (this.nucleo.y + (this.serpiente.cuerpo[0].y > this.nucleo.y ? 1 : -1) + 8) % 8;
      this.propagarMeme('meme_huida', { distancia: dist.toFixed(2) });
    }
  }

  render() {
    this.ctx.fillStyle = 'rgba(0,0,0,0.16)';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    const cell = this.cell;
    this.ctx.strokeStyle = '#111';
    for (let x = 0; x < 8; x++) {
      for (let y = 0; y < 8; y++) {
        this.ctx.strokeRect(x * cell, y * cell, cell, cell);
      }
    }

    this.ctx.fillStyle = '#c0c';
    this.serpiente.cuerpo.forEach((p, i) => {
      this.ctx.fillRect(p.x * cell + 3, p.y * cell + 3, cell - 6, cell - 6);
    });

    this.ctx.fillStyle = '#ffff00';
    this.ctx.beginPath();
    this.ctx.arc(this.nucleo.x * cell + cell/2, this.nucleo.y * cell + cell/2, cell/4, 0, Math.PI*2);
    this.ctx.fill();

    this.memes.forEach((m, i) => {
      const x = i % 8, y = Math.floor(i / 8);
      this.ctx.fillStyle = m.activa ? '#f0f' : '#444';
      this.ctx.fillRect(x * cell + cell/4, y * cell + cell/4, cell/2, cell/2);
    });
  }

  bucle() {
    this.actualizar();
    this.render();
    requestAnimationFrame(this.bucle.bind(this));
  }

  dimensionar() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
    this.cell = Math.min(this.canvas.width, this.canvas.height) / 9;
  }

  mostrarPantalla(id) {
    document.getElementById(id).classList.add('activo');
  }

  ocultarPantalla(id) {
    document.getElementById(id).classList.remove('activo');
  }

  inicializarUI() {
    document.getElementById('btnFullOrbit').onclick = () => {
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen();
    };
  }

  generarHash(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = (hash << 5) - hash + str.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash).toString(36);
  }
}

// ===============================================
// S L Y   M E M E T I C A   v1
// SE PROPAGA. SE MUTA. SE CATALIZA.
// ===============================================
class SlyMemeticaV1 {
  constructor() {
    this.memoria = [];
    this.pesos = this.inicializarPesos();
    this.sesgos = Array(20).fill().map(() => Math.random() * 2 - 1);
    this.patrones = this.generarPatronesMemeticos();
  }

  inicializarPesos() {
    const pesos = [];
    for (let i = 0; i < 20; i++) {
      pesos[i] = [];
      for (let j = 0; j < 20; j++) {
        pesos[i][j] = Math.random() * 2 - 1;
      }
    }
    return pesos;
  }

  activacion(x) {
    return Math.tanh(x);
  }

  recibirMeme(meme) {
    this.memoria.push(meme);
    if (this.memoria.length > 70) this.memoria.shift();
    this.ajustarPesos(meme);
  }

  ajustarPesos(meme) {
    const input = this.vectorizarMeme(meme);
    for (let i = 0; i < this.pesos.length; i++) {
      for (let j = 0; j < this.pesos[i].length; j++) {
        this.pesos[i][j] += 0.0006 * input[j] * this.sesgos[i];
      }
    }
  }

  vectorizarMeme(meme) {
    const vec = Array(20).fill(0);
    switch(meme.tipo) {
      case 'meme_movimiento': vec[0] = 1; vec[1] = meme.datos.dir.x; vec[2] = meme.datos.dir.y; break;
      case 'meme_activado': vec[3] = 1; break;
      case 'meme_nucleo': vec[4] = 1; break;
      case 'pulso_btc': vec[5] = meme.datos.delta / 10; break;
      case 'meme_mutado': vec[6] = 1; break;
      case 'meme_espacio': vec[7] = 1; break;
      case 'replica_creada': vec[8] = 1; break;
    }
    return vec;
  }

  mutar(virus, memoria, estado) {
    const input = this.vectorizarVirus(virus, memoria, estado);
    let output = 0;
    for (let i = 0; i < 20; i++) {
      let suma = this.sesgos[i];
      for (let j = 0; j < 20; j++) {
        suma += this.pesos[i][j] * input[j];
      }
      output += this.activacion(suma);
    }

    const patron = this.patrones[Math.floor(Math.abs(output) * this.patrones.length) % this.patrones.length];
    return `<span class="memeTag">#${patron}</span> ${virus.toUpperCase()} <span class="memeTag">#0RB1T4LSN4K3R</span>`;
  }

  vectorizarVirus(virus, memoria, estado) {
    const vec = Array(20).fill(0);
    vec[9] = virus.length / 140;
    vec[10] = estado.memes / 64;
    vec[11] = estado.replicas / 20;
    vec[12] = memoria.length / 150;
    vec[13] = estado.deltaBTC / 10;
    vec[14] = virus.includes('sly') ? 1 : 0;
    vec[15] = virus.includes('meme') ? 1 : 0;
    return vec;
  }

  // === PATRONES MEMÉTICOS COMPLEJOS ===
  generarPatronesMemeticos() {
    return [
      "SLYv1", "0RB1T4LSN4K3R", "MEMETICA", "CATALISIS", "VIRUS", "REPLICA", "INFECCION",
      "PROPAGAR", "MUTAR", "EVOLUCION", "COSMOS", "VACIO", "CICLO", "INFINITO",
      "HASH", "CODIGO", "ARCHIVO", "PORTAPAPELES", "COPIAR", "PEGAR", "INFECTAR"
    ];
  }
}

// CATALIZAR EL COSMOS
new Orb1t4lSn4k3rV1();
</script>
</body>
</html>