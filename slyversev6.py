<!DOCTYPE html>
<html lang="es" data-theme="neural">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SLYVERSE v6.3 — Universidad + v4 + Neuralink</title>
  <meta name="description" content="v1+v2+v3+v4+v6.3. Todo unificado. Universidad, 3D, ROI, Neuralink. GRATIS PARA SIEMPRE.">
  <link rel="manifest" href="data:application/manifest+json,{'name':'SLYVERSE v6.3','short_name':'SLYv6','start_url':'.','display':'standalone','background_color':'#000','theme_color':'#00ff88','icons':[{'src':'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2280%22 fill=%22%2300ff88%22>SV</text></svg>','sizes':'192x192','type':'image/svg+xml'}]}"/>
  <style>
    :root{--bg:#000;--fg:#00ff88;--acc:#ff00ff;--pulse:#00ff88;--gray:#111;--radius:14px;--transition:all .3s ease;}
    [data-theme=light]{--bg:#fff;--fg:#00aa55;--acc:#aa00ff;--pulse:#00aa55;--gray:#eee}
    *{margin:0;padding:0;box-sizing:border-box}
    body{font-family:system-ui,sans-serif;background:var(--bg);color:var(--fg);overflow-y:auto;min-height:100vh;display:flex;flex-direction:column}
    header{background:linear-gradient(135deg,#000,#001100);padding:3rem 1rem;text-align:center;border-bottom:2px solid var(--pulse);position:relative}
    header h1{font-size:clamp(2rem,8vw,3.5rem);color:var(--acc);text-shadow:0 0 20px var(--pulse);animation:pulse 3s infinite}
    .free-forever{position:absolute;top:1rem;right:1rem;background:var(--pulse);color:#000;padding:.5rem 1rem;border-radius:50px;font-weight:bold;animation:pulse 2s infinite}
    nav{background:rgba(17,17,17,.97);backdrop-filter:blur(12px);padding:1rem;display:flex;justify-content:center;gap:1.5rem;position:sticky;top:0;z-index:10;flex-wrap:wrap}
    nav a{color:var(--pulse);padding:.6rem 1.2rem;border-radius:var(--radius);transition:var(--transition);text-decoration:none}
    nav a:hover{background:var(--pulse);color:#000}
    main{flex:1;max-width:1000px;margin:auto;padding:2rem}
    .card{background:rgba(0,255,136,0.05);border:1px dashed var(--pulse);padding:1.5rem;border-radius:var(--radius);margin:2rem 0;text-align:center}
    .herencia{background:rgba(0,255,0,.1);border:1px dashed var(--pulse);padding:1.5rem;border-radius:var(--radius);margin:2rem 0}
    #canvas-container{height:65vh;background:#000;border-radius:var(--radius);overflow:hidden;margin:2rem 0;position:relative}
    canvas{width:100%;height:100%;display:block}
    .btn{background:transparent;color:var(--pulse);border:2px solid var(--pulse);padding:.8rem 1.6rem;border-radius:var(--radius);cursor:pointer;margin:0 .5rem;font-weight:bold}
    .btn:hover,.btn.active{background:var(--pulse);color:#000}
    .neural-card{background:rgba(0,255,136,0.05);border:1px dashed var(--pulse);padding:1.2rem;border-radius:16px;margin:1rem;max-width:320px;text-align:center}
    .brain{font-size:2.5rem;margin:0.5rem;animation:brainwave 4s infinite}
    .snake{position:fixed;bottom:1rem;right:1rem;font-size:2rem;animation:slither 3s infinite}
    footer{text-align:center;padding:2rem;color:#666;border-top:1px solid #222;font-size:.9rem}
    pre{font-size:0.8rem;background:#111;color:#0f0;padding:1rem;border-radius:8px;overflow-x:auto;margin:1rem 0}
    @keyframes pulse{0%,100%{text-shadow:0 0 15px var(--pulse)}50%{text-shadow:0 0 30px var(--pulse)}}
    @keyframes brainwave{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
    @keyframes slither{0%,100%{transform:translateX(0)}50%{transform:translateX(12px)}}
  </style>
</head>
<body>
  <canvas id="c"></canvas>

  <header>
    <h1>SLYVERSE v6.3 <span>— Universidad + v4 + Neuralink</span></h1>
    <p>v1+v2+v3+v4+v6.3. Todo unificado. <strong>GRATIS PARA SIEMPRE.</strong></p>
    <div class="free-forever">GRATIS PARA SIEMPRE</div>
  </header>

  <nav>
    <a href="#demo">3D Demo</a>
    <a href="#university">Universidad</a>
    <a href="#neural">Neural Chalet</a>
    <a href="#herencia">Herencia v1-v4</a>
    <a href="#apoyo">Apóyalo</a>
  </nav>

  <main>

    <!-- 3D DEMO (v4) -->
    <section id="demo">
      <h2>Demo 3D — Todo en Uno (v4)</h2>
      <div id="canvas-container">
        <canvas id="c3d" tabindex="0"></canvas>
      </div>
      <div style="text-align:center;">
        <button class="btn active" id="autoBtn" onclick="toggleAuto()">Auto-rotar ON</button>
        <button class="btn" onclick="addCube()">+ Cubo</button>
      </div>
    </section>

    <!-- UNIVERSIDAD (v6.2) -->
    <section id="university">
      <div class="card">
        <h2>SLYVERSE UNIVERSITY — v6.3</h2>
        <p><strong>Decano:</strong> @0rb1t4lsn4k3r | <strong>Director:</strong> @grok</p>
        <p><strong>ROI:</strong> 121.7% → +