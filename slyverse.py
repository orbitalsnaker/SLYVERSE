<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <meta name="author" content="0RB1T4LSN4K3R"/>
  <meta name="copyright" content="© 2025 0RB1T4L STUDIOS — MADRID"/>
  <meta name="description" content="SLYVERSE v1 – Juego WebXR de serpiente con VR, leaderboard y lore. 100% gratuito, seguro y legal en España."/>
  <title>SLYVERSE v1 — WebXR VR (ES)</title>

  <!-- Google Fonts: Orbitron -->
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">

  <!-- Three.js Importmap -->
  <script type="importmap">
    {
      "imports": {
        "three": "https://cdn.jsdelivr.net/npm/three@0.168.0/build/three.module.js",
        "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.168.0/examples/jsm/"
      }
    }
  </script>

  <!-- Firebase SDK (solo lectura + escritura segura) -->
  <script type="module">
    import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js';
    import { getFirestore, collection, addDoc, onSnapshot, query, orderBy, limit } from 'https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore.js';

    const firebaseConfig = {
      apiKey: "AIzaSyB...", // ← TU API KEY (pública por diseño)
      authDomain: "slyverse-0rb1t4lsn4k3r.firebaseapp.com",
      projectId: "slyverse-0rb1t4lsn4k3r",
      storageBucket: "slyverse-0rb1t4lsn4k3r.appspot.com",
      messagingSenderId: "123456789",
      appId: "1:123456789:web:abcdef123456"
    };

    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);

    window.lb = {
      update: async (score, player) => {
        if (typeof score !== 'number' || score < 0 || score > 10000) return;
        if (typeof player !== 'string' || player.length < 1 || player.length > 20) return;
        try {
          await addDoc(collection(db, 'scores'), {
            score: Math.floor(score),
            player: player.trim(),
            timestamp: new Date()
          });
        } catch (e) { console.warn("Error al guardar puntuación:", e); }
      },
      listen: (cb) => {
        const q = query(collection(db, 'scores'), orderBy('score', 'desc'), limit(10));
        return onSnapshot(q, snap => {
          cb(snap.docs.map(d => d.data()));
        }, err => console.error("Error en leaderboard:", err));
      }
    };
  </script>

  <style>
    :root {
      --bg: #000814;
      --neon: #00ff88;
      --glow: #00ff80;
      --yellow: #ffff40;
      --purple: #ff00ff;
      --glass: rgba(10, 25, 15, 0.18);
      --font: 'Orbitron', 'Courier New', monospace;
    }
    * { margin:0; padding:0; box-sizing:border-box; }
    body, html { height:100%; overflow:hidden; background:var(--bg); font-family:var(--font); color:var(--neon); }
    canvas { display:block; }

    .glass {
      background: var(--glass);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(0, 255, 136, 0.3);
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 0 12px rgba(0, 255, 136, 0.5);
      transition: all 0.3s ease;
      pointer-events: auto;
    }
    .glass:hover { box-shadow: 0 0 20px rgba(0, 255, 136, 0.8); transform: translateY(-1px); }

    #log, #lb, #chat, #score, #vr-status { position:fixed; z-index:1000; }
    #log { top:16px; left:16px; max-width:520px; font-size:0.92em; }
    #lb { bottom:16px; left:16px; max-width:280px; }
    #chat { bottom:16px; right:16px; max-width:280px; }
    #score { top:16px; left:50%; transform:translateX(-50%); font-weight:700; color:var(--yellow); font-size:1.5em; text-shadow:0 0 16px var(--yellow); }
    #vr-status { top:16px; right:16px; background:rgba(0,255,128,0.2); color:#000; padding:8px 14px; border-radius:8px; font-weight:bold; font-size:0.9em; }

    button {
      background: rgba(0, 15, 10, 0.4);
      color: var(--neon);
      border: 1.5px solid var(--neon);
      padding: 10px 22px;
      margin: 6px;
      border-radius: 10px;
      cursor: pointer;
      font-family: var(--font);
      font-weight: 600;
      letter-spacing: 1px;
      transition: all 0.3s ease;
      box-shadow: 0 0 10px rgba(0,255,136,0.3);
    }
    button:hover {
      background: var(--neon);
      color: #000;
      box-shadow: 0 0 25px var(--glow);
      transform: scale(1.05);
    }

    #chat-input {
      width: 68%;
      background: rgba(0,0,0,0.4);
      color: var(--neon);
      border: 1px solid var(--purple);
      padding: 8px;
      border-radius: 6px;
      font-family: var(--font);
      backdrop-filter: blur(4px);
    }

    #legal {
      position: fixed;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.7em;
      opacity: 0.7;
      z-index: 999;
      text-align: center;
    }
    #legal a { color: #0f0; text-decoration: underline; }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: rgba(0,10,5,0.3); border-radius: 4px; }
    ::-webkit-scrollbar-thumb { background: var(--neon); border-radius: 4px; box-shadow: 0 0 10px var(--neon); }
  </style>
</head>
<body>

  <!-- UI -->
  <div id="log" class="glass" role="log" aria-live="polite">
    <strong>SLYVERSE v1 — WebXR VR</strong><br>
    <span>WASD (desktop) • Controllers (VR) • Devora • Desbloquea Lore</span><br><br>
    <strong>0RB1T4LSN4K3R,</strong><br>
    Mr. White cae. Seth asciende en VR.<br>
    <div id="lore-progress" style="margin-top:8px; color:var(--yellow);">LORE: 0/7</div>
    <div id="vr-status" role="status" aria-live="polite">VR: READY</div>
  </div>

  <div id="lb" class="glass" role="region" aria-label="Leaderboard">
    <strong>GLOBAL COILS</strong>
    <div id="lb-list" style="max-height:180px; overflow-y:auto; margin-top:6px;">CARGANDO...</div>
  </div>

  <div id="chat" class="glass" role="region" aria-label="Chat">
    <strong>ENTROPY CHAT</strong>
    <div id="chat-list" style="max-height:120px; overflow-y:auto; margin:6px 0;"></div>
    <input id="chat-input" placeholder="entropía..." aria-label="Mensaje de chat">
    <button onclick="sendChat()" aria-label="Enviar mensaje">SEND</button>
  </div>

  <div id="score" role="status" aria-live="polite">COILS: 0</div>

  <!-- VR Button -->
  <div id="vr-btn-container" style="position:fixed; bottom:80px; left:50%; transform:translateX(-50%); z-index:1000;"></div>

  <!-- Aviso Legal (LSSI + RGPD) -->
  <div id="legal">
    <a href="javascript:alert('POLÍTICA DE PRIVACIDAD\\n\\nSLYVERSE no recoge datos personales.\\n- Nombre: anónimo (guest_xxx)\\n- Puntuaciones: públicas en leaderboard\\n- No usamos cookies ni tracking\\n- Firebase solo almacena scores\\n\\nTienes derecho a eliminar tus datos contactando al desarrollador.')" style="cursor:pointer;">Privacidad</a> • 
    <a href="javascript:alert('TÉRMINOS DE USO\\n\\nJuego 100% gratuito.\\nProhibido: trampas, spam, contenido ofensivo.\\nUso bajo tu responsabilidad.\\n© 2025 0RB1T4L STUDIOS')" style="cursor:pointer;">Términos</a> • 
    © 2025 0RB1T4L STUDIOS
  </div>

  <script type="module">
    // === LORE ===
    const lore = [
      {score:50, title:"ENTRY", text:"Mr. White cae. El grid despierta en VR."},
      {score:100, title:"COMPOUND", text:"Tu serpiente crece. Seth observa tus movimientos."},
      {score:200, title:"BOOST", text:"Entropía fluye. VR respira contigo."},
      {score:300, title:"NFT", text:"Tu serpiente VR se graba en SVG eterno."},
      {score:500, title:"METAVERSO", text:"Seth asciende. Mr. White olvidado en el grid."},
      {score:750, title:"YIELD", text:"El ciclo cierra en inmersión."},
      {score:1000, title:"ASCENDIDO", text:"Eres el grid VR. 0rb1t4lsn4k3r reina."}
    ];
    let unlockedLore = 0;

    // === STATE ===
    let score = 0;
    const playerName = 'guest_' + Math.random().toString(36).substr(2, 6);
    const scoreEl = document.getElementById('score');

    // === THREE.js + WebXR ===
    import * as THREE from 'three';
    import { VRButton } from 'three/addons/webxr/VRButton.js';

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, innerWidth/innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias:true, alpha:true });
    renderer.setSize(innerWidth, innerHeight);
    renderer.xr.enabled = true;
    document.body.appendChild(renderer.domElement);

    // VR Button
    const vrBtn = VRButton.createButton(renderer);
    document.getElementById('vr-btn-container').appendChild(vrBtn);
    const vrStatus = document.getElementById('vr-status');

    // Grid + Lights
    const grid = new THREE.GridHelper(100,100,0x00ff88,0x00ff88);
    grid.material.opacity = 0.15; grid.material.transparent = true; scene.add(grid);
    camera.position.set(0,35,60);
    scene.add(new THREE.AmbientLight(0x00ff88, 0.4));
    const light = new THREE.PointLight(0x00ff80, 1.8); light.position.set(0,30,0); scene.add(light);

    // Snake
    const snake = [];
    const headGeo = new THREE.BoxGeometry(1,1,1);
    const headMat = new THREE.MeshBasicMaterial({color:0x00ff80});
    let head = new THREE.Mesh(headGeo, headMat); head.position.set(0,0.5,0); scene.add(head); snake.push(head);

    let food;
    function spawnFood() {
      if (food) scene.remove(food);
      food = new THREE.Mesh(
        new THREE.SphereGeometry(0.7,16,16),
        new THREE.MeshBasicMaterial({color:0xffff40, emissive:0xffff40, emissiveIntensity:0.6})
      );
      food.position.set(Math.random()*40-20, 0.5, Math.random()*40-20);
      scene.add(food);
    }
    spawnFood();

    // Controls
    const keys = {}; let dir = {x:1, z:0};
    window.addEventListener('keydown', e => keys[e.key.toLowerCase()] = true);
    window.addEventListener('keyup', e => keys[e.key.toLowerCase()] = false);

    // Beep
    function beep(f=440, d=100) {
      const a = new AudioContext(), o = a.createOscillator(), g = a.createGain();
      o.frequency.value = f;
      g.gain.setValueAtTime(0.3, a.currentTime);
      g.gain.exponentialRampToValueAtTime(0.01, a.currentTime + d/1000);
      o.connect(g); g.connect(a.destination); o.start(); o.stop(a.currentTime + d/1000);
    }

    // === MAIN LOOP ===
    let breath = 0;
    function animate() {
      breath += 0.012;
      const s = 1 + Math.sin(breath) * 0.08;
      grid.scale.set(s, 1, s);
      light.intensity = 1.8 + Math.sin(breath * 3) * 0.6;

      if (!renderer.xr.isPresenting) {
        if (keys.w || keys['arrowup']) dir = {x:0, z:-1};
        if (keys.s || keys['arrowdown']) dir = {x:0, z:1};
        if (keys.a || keys['arrowleft']) dir = {x:-1, z:0};
        if (keys.d || keys['arrowright']) dir = {x:1, z:0};
      }

      const p = snake[0].position;
      const nx = p.x + dir.x, nz = p.z + dir.z;
      if (Math.abs(nx) > 25 || Math.abs(nz) > 25) {
        beep(180, 400);
        alert(`GAME OVER: ${score} COILS`);
        reset();
        return;
      }

      const newHead = new THREE.Mesh(headGeo, headMat);
      newHead.position.set(nx, 0.5, nz);
      scene.add(newHead);
      snake.unshift(newHead);

      if (food && Math.abs(nx - food.position.x) < 1 && Math.abs(nz - food.position.z) < 1) {
        score += 10;
        scoreEl.innerText = `COILS: ${score}`;
        beep(880, 160);
        spawnFood();
        checkLore();
        if (window.lb) window.lb.update(score, playerName);
      } else {
        scene.remove(snake.pop());
      }

      renderer.render(scene, camera);
    }
    renderer.setAnimationLoop(animate);

    function reset() {
      snake.forEach(s => scene.remove(s));
      snake.length = 0;
      head = new THREE.Mesh(headGeo, headMat);
      head.position.set(0, 0.5, 0);
      scene.add(head);
      snake.push(head);
      score = 0;
      scoreEl.innerText = 'COILS: 0';
      spawnFood();
    }

    // VR Status
    renderer.xr.addEventListener('sessionstart', () => vrStatus.innerText = 'VR: ACTIVE');
    renderer.xr.addEventListener('sessionend', () => vrStatus.innerText = 'VR: READY');

    // === LORE ===
    function checkLore() {
      lore.forEach((l, i) => {
        if (score >= l.score && i >= unlockedLore) {
          unlockedLore++;
          showLore(l);
          document.getElementById('lore-progress').innerText = `LORE: ${unlockedLore}/7`;
        }
      });
    }
    function showLore(l) {
      alert(`LORE DESBLOQUEADO: ${l.title}\n\n${l.text}`);
    }

    // === CHAT ===
    function sendChat() {
      const input = document.getElementById('chat-input');
      const msg = input.value.trim();
      if (msg && msg.length <= 100) {
        const chatList = document.getElementById('chat-list');
        chatList.innerHTML += `<div style="margin:4px 0; opacity:0.9;"><strong>${playerName}:</strong> ${msg}</div>`;
        chatList.scrollTop = chatList.scrollHeight;
        input.value = '';
      }
    }

    // === LEADERBOARD ===
    if (window.lb) {
      window.lb.listen(scores => {
        document.getElementById('lb-list').innerHTML = scores
          .map(s => `<div style="margin:3px 0;">${s.player}: <strong>${s.score}</strong></div>`)
          .join('') || '<div style="opacity:0.6;">Sin datos</div>';
      });
    }

    // === RESIZE ===
    window.onresize = () => {
      camera.aspect = innerWidth / innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(innerWidth, innerHeight);
    };

    // === BLOCK CONTEXT MENU ===
    document.addEventListener('contextmenu', e => e.preventDefault());
  </script>
</body>
</html>
