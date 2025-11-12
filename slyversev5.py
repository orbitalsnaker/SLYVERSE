<!DOCTYPE html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SLYVERSE v5 — El Chalet Ético | DAO + AR</title>
  <meta name="description" content="Si Ismael cierra, cocreamos. Chalet 3D + $SLY DAO. 100% libre.">
  <link rel="manifest" href="data:application/manifest+json,{'name':'SLYVERSE v5','short_name':'SLYv5','start_url':'.','display':'standalone','background_color':'#0a0a0a','theme_color':'#00ff41','icons':[{'src':'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22 fill=%22%230f0%22>Chalet</text></svg>','sizes':'192x192','type':'image/svg+xml'}]}"/>
  <style>
    :root{--bg:#0a0a0a;--fg:#00ff41;--acc:#ff00ff;--gold:#ffd700;--gray:#333}
    [data-theme=light]{--bg:#fafafa;--fg:#000;--acc:#00aaff;--gold:#b8860b;--gray:#ccc}
    *{margin:0;padding:0;box-sizing:border-box}
    body{font-family:system-ui,sans-serif;background:var(--bg);color:var(--fg);overflow:hidden;height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center}
    canvas{width:100%;height:100%;position:absolute;top:0;left:0;z-index:-1}
    .ui{position:absolute;top:0;left:0;right:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:1rem;pointer-events:none}
    .top,.mid,.bottom{pointer-events:auto;text-align:center}
    h1{font-size:1.4rem;margin:0.5rem;color:var(--acc);text-shadow:0 0 10px var(--acc)}
    .card{background:rgba(255,255,255,0.1);padding:0.8rem;border-radius:12px;margin:0.5rem;max-width:300px}
    .sly{color:var(--gold);font-weight:bold}
    button{background:var(--acc);color:var(--bg);border:none;padding:0.6rem 1.2rem;border-radius:50px;font-weight:bold;margin:0.3rem;cursor:pointer;pointer-events:auto;font-size:0.8rem}
    .toggle{position:absolute;top:1rem;right:1rem;background:var(--gray);color:var(--fg);padding:0.5rem;border-radius:50%}
    .snake{position:absolute;bottom:1rem;font-size:1.8rem;animation:slither 3s infinite}
    @keyframes slither{0%,100%{transform:translateX(0)}50%{transform:translateX(10px)}}
  </style>
</head>
<body>
  <canvas id="c"></canvas>
  <div class="ui">
    <div class="top">
      <h1>SLYVERSE v5 — El Chalet Ético</h1>
      <p>DAO + AR + $SLY | Si Ismael cierra, cocreamos.</p>
    </div>
    <div class="mid" id="chaletCard">
      <div class="card">
        <div><strong>Chalet Ético</strong></div>
        <div>4 hab · Jardín verde · 100% DAO</div>
        <div class="sly">Aval: <span id="votes">0</span> $SLY</div>
        <button onclick="vote()">+1 $SLY (tienes <span id="wallet">0</span>)</button>
        <button onclick="claimKonami()">Konami → +5 $SLY</button>
      </div>
    </div>
    <div class="bottom">
      <button onclick="enterAR()">Entrar en AR</button>
      <button onclick="toggleTheme()">Toggle</button>
      <div class="snake">Snake</div>
    </div>
  </div>

  <script type="module">
    import { init, animate, addLadrillo } from 'https://cdn.jsdelivr.net/gh/orbitalsnaker/slyverse-v5@main/chalet.js';
    import { connectWallet, mintSLY, voteOnChalet } from 'https://cdn.jsdelivr.net/gh/orbitalsnaker/slyverse-v5@main/dao.js';

    const c = document.getElementById('c'), ctx = c.getContext('2d');
    let w, h, rot = 0, votes = 0, wallet = 0;
    const konami = '38,38,40,40,37,39,37,39,66,65'; let k = [];

    // Resize
    function resize(){w=c.width=window.innerWidth;h=c.height=window.innerHeight}
    resize(); window.addEventListener('resize',resize);

    // 3D Chalet (simplificado)
    const chalet = {x:0,y:0,z:5,size:2,color:'#00ff41'};
    function project(x,y,z){const scale=200/(200+z+300);return{x:w/2+x*scale,y:h/2+y*scale,s:scale}}
    function drawCube(cube){/* mismo que v4, reutilizado */}
    function animate3D(){
      ctx.fillStyle='rgba(10,10,10,0.1)'; ctx.fillRect(0,0,w,h);
      rot+=0.01; chalet.z=Math.cos(rot*0.8)*3;
      drawCube(chalet);
      requestAnimationFrame(animate3D);
    }
    animate3D();

    // UI
    function updateUI(){document.getElementById('votes').textContent=votes;document.getElementById('wallet').textContent=wallet}
    function vote(){
      if(wallet<1) return alert('¡Necesitas $SLY! Usa Konami.');
      wallet--; votes++; updateUI();
      addLadrillo(); voteOnChalet(votes);
      if(votes>=50) alert('¡Chalet CERTIFIED! DAO Senate SLY activado. Article 27 aprobado.');
    }
    function claimKonami(){wallet+=5; updateUI(); alert('Snake +5 $SLY!'); k=[]}

    // Konami
    document.addEventListener('keydown', e=>{k.push(e.keyCode);if(k.toString().indexOf(konami)>=0) claimKonami()});

    // AR
    function enterAR(){
      if(navigator.xr && navigator.xr.isSessionSupported('immersive-ar')){
        navigator.xr.requestSession('immersive-ar').then(s=>init(s));
      } else alert('Gira con dedo. Chalet 3D listo. ¡Konami = +5 $SLY!');
    }

    // DAO (mock)
    async function initDAO(){try{await connectWallet(); wallet=await mintSLY(10);}catch(e){console.log('Wallet no conectado')}}; initDAO();

    function toggleTheme(){
      const isDark=document.documentElement.getAttribute('data-theme')==='dark';
      document.documentElement.setAttribute('data-theme',isDark?'light':'dark');
    }

    updateUI();
  </script>
</body>
</html>