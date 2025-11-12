<!DOCTYPE html>
<html lang="es" data-theme="neural">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SLYVERSE v6 — Neural Chalet | Pensamiento → Realidad</title>
  <meta name="description" content="Neuralink + SLYVERSE. Piensa el hogar, cocrea el futuro. v6 dormida hasta el día del implante.">
  <link rel="manifest" href="data:application/manifest+json,{'name':'SLYVERSE v6','short_name':'SLYv6','start_url':'.','display':'standalone','background_color':'#000000','theme_color':'#00ff88','icons':[{'src':'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2280%22 fill=%22%2300ff88%22>Neural</text></svg>','sizes':'192x192','type':'image/svg+xml'}]}"/>
  <style>
    :root{--bg:#000000;--fg:#00ff88;--acc:#ff00ff;--pulse:#00ff88;--gray:#111}
    [data-theme=light]{--bg:#ffffff;--fg:#00aa55;--acc:#aa00ff;--pulse:#00aa55;--gray:#eee}
    *{margin:0;padding:0;box-sizing:border-box}
    body{font-family:system-ui,sans-serif;background:var(--bg);color:var(--fg);overflow:hidden;height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}
    canvas{width:100%;height:100%;position:absolute;top:0;left:0;z-index:-1;opacity:0.7}
    .ui{position:absolute;top:0;left:0;right:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:1rem;pointer-events:none}
    .top,.mid,.bottom{pointer-events:auto;text-align:center}
    h1{font-size:1.4rem;margin:0.5rem;color:var(--acc);text-shadow:0 0 15px var(--pulse);animation:pulse 3s infinite}
    .neural-card{background:rgba(0,255,136,0.05);border:1px dashed var(--pulse);padding:1.2rem;border-radius:16px;margin:1rem;max-width:320px;text-align:center}
    .brain{font-size:2.5rem;margin:0.5rem;animation:brainwave 4s infinite}
    button{background:var(--acc);color:#000;border:none;padding:0.7rem 1.4rem;border-radius:50px;font-weight:bold;margin:0.4rem;cursor:pointer;pointer-events:auto;font-size:0.9rem;opacity:0.6}
    button.active{opacity:1;background:var(--pulse);color:#000}
    .toggle{position:absolute;top:1rem;right:1rem;background:var(--gray);color:var(--fg);padding:0.5rem;border-radius:50%;opacity:0.6}
    .snake{position:absolute;bottom:1rem;font-size:2rem;animation:slither 3s infinite}
    @keyframes pulse{0%,100%{text-shadow:0 0 15px var(--pulse)}50%{text-shadow:0 0 30px var(--pulse)}}
    @keyframes brainwave{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
    @keyframes slither{0%,100%{transform:translateX(0)}50%{transform:translateX(12px)}}
  </style>
</head>
<body>
  <canvas id="c"></canvas>
  <div class="ui">
    <div class="top">
      <h1>SLYVERSE v6 — Neural Chalet</h1>
      <p>Pensamiento → Realidad | Dormida hasta Neuralink</p>
    </div>
    <div class="mid">
      <div class="neural-card">
        <div class="brain">🧠</div>
        <div><strong>Estado: Dormida</strong></div>
        <div>Esperando señal Neuralink...</div>
        <div style="font-size:0.8rem;margin-top:0.5rem;color:var(--pulse)">
          Piensa: "Despierta v6" → activa el chalet
        </div>
        <button id="wakeBtn" onclick="wakeNeural()">🧠 Despertar (simulación)</button>
      </div>
    </div>
    <div class="bottom">
      <button onclick="enterMind()">Entrar en Mente</button>
      <button onclick="toggleTheme()">Toggle</button>
      <div class="snake">Snake</div>
    </div>
  </div>

  <script>
    const c = document.getElementById('c'), ctx = c.getContext('2d');
    let w, h, rot = 0, neuralActive = false;
    let brainSignal = 0, chalet = {x:0,y:0,z:5,size:2,color:'#00ff88'};

    function resize(){w=c.width=window.innerWidth;h=c.height=window.innerHeight}
    resize(); window.addEventListener('resize',resize);

    // Fondo neural
    function drawNeural(){
      ctx.fillStyle = 'rgba(0,255,136,0.02)'; ctx.fillRect(0,0,w,h);
      rot += 0.005;
      const pulse = Math.sin(rot*3)*0.5+0.5;
      ctx.strokeStyle = `rgba(0,255,136,${pulse*0.3})`;
      ctx.lineWidth = 1;
      for(let i=0;i<50;i++){
        const x = Math.random()*w, y = Math.random()*h;
        ctx.beginPath(); ctx.arc(x,y,pulse*20,0,Math.PI*2); ctx.stroke();
      }
    }

    // Chalet 3D (solo al despertar)
    function project(x,y,z){
      const scale = 200 / (200 + z + 300);
      return {x: w/2 + x*scale, y: h/2 + y*scale, s:scale};
    }
    function drawCube(cube){
      const s = cube.size, v = [
        project(-s+cube.x,-s+cube.y,-s+cube.z),
        project( s+cube.x,-s+cube.y,-s+cube.z),
        project( s+cube.x, s+cube.y,-s+cube.z),
        project(-s+cube.x, s+cube.y,-s+cube.z),
        project(-s+cube.x,-s+cube.y, s+cube.z),
        project( s+cube.x,-s+cube.y, s+cube.z),
        project( s+cube.x, s+cube.y, s+cube.z),
        project(-s+cube.x, s+cube.y, s+cube.z)
      ];
      const faces = [[0,1,2],[0,2,3],[4,5,6],[4,6,7],[0,1,5],[0,5,4],[1,2,6],[1,6,5],[2,3,7],[2,7,6],[3,0,4],[3,4,7]];
      faces.forEach(f => {
        const [a,b,c] = [v[f[0]], v[f[1]], v[f[2]]];
        if (a && b && c) {
          ctx.fillStyle = cube.color; ctx.globalAlpha = 0.6;
          ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.lineTo(c.x,c.y); ctx.closePath(); ctx.fill();
        }
      });
    }

    function animate(){
      drawNeural();
      if(neuralActive){
        rot += 0.01;
        chalet.z = Math.cos(rot*0.8)*3 + 5;
        drawCube(chalet);
      }
      requestAnimationFrame(animate);
    }
    animate();

    // Neuralink Simulación
    function wakeNeural(){
      neuralActive = true;
      document.getElementById('wakeBtn').textContent = '🧠 v6 DESPIERTA';
      document.getElementById('wakeBtn').classList.add('active');
      alert('¡Neuralink detectado! Pensamiento: "Chalet Ético". v6 activa. Cocreamos con la mente.');
    }

    function enterMind(){
      if(neuralActive){
        alert('Entrando en el chalet neural... Piensa: "Jardín verde" → crece.');
      } else {
        alert('Neuralink dormida. Usa Konami → simula señal cerebral.');
      }
    }

    // Konami = simula Neuralink
    let k = []; const konami = '38,38,40,40,37,39,37,39,66,65';
    document.addEventListener('keydown', e=>{
      k.push(e.keyCode);
      if(k.toString().indexOf(konami)>=0){
        wakeNeural();