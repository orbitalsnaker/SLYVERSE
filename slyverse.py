#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import subprocess
from datetime import datetime
import pytz

OUTPUT_FILE = "slyverse.html"
WALLET_ADDRESS = "0x2bd4e0e310436b7ea9944f2edff25b665cea2fea"
FIREBASE_CONFIG = {
    "apiKey": "AIzaSyB...",
    "authDomain": "slyverse-0rb1t4lsn4k3r.firebaseapp.com",
    "projectId": "slyverse-0rb1t4lsn4k3r",
    "storageBucket": "slyverse-0rb1t4lsn4k3r.appspot.com",
    "messagingSenderId": "123456789",
    "appId": "1:123456789:web:abcdef123456"
}

tz = pytz.timezone('Europe/Madrid')
now = datetime.now(tz)
LOCAL_TIME = now.strftime("%d %b %Y %H:%M") + (" CEST" if now.dst() else " CET")

FIRESTORE_RULES = """rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /scores/{doc} {
      allow read: if true;
      allow write: if request.auth == null
                  && request.resource.data.keys().hasOnly(['score','player','timestamp'])
                  && request.resource.data.score is int
                  && request.resource.data.score >= 0
                  && request.resource.data.score <= 10000
                  && request.resource.data.player is string
                  && request.resource.data.player.size() >= 1
                  && request.resource.data.player.size() <= 20
                  && request.resource.data.player.matches('^[a-zA-Z0-9_]+$')
                  && request.resource.data.timestamp is timestamp
                  && request.time <= request.resource.data.timestamp + duration.value(5,'s')
                  && request.time >= timestamp.date(2025,1,1);
    }
  }
}
"""

HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="author" content="0RB1T4LSN4K3R"/>
<meta name="copyright" content="© 2025 0RB1T4L STUDIOS — MADRID"/>
<meta name="description" content="SLYVERSE v1 – Juego WebXR de serpiente con VR, leaderboard y lore. 100% gratuito, seguro y legal en España."/>
<title>SLYVERSE v1 — WebXR VR (ES)</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
<script type="importmap">{{"imports":{{"three":"https://cdn.jsdelivr.net/npm/three@0.168.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.168.0/examples/jsm/"}}}}</script>
<script type="module">
import {{initializeApp}} from 'https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js';
import {{getFirestore,collection,addDoc,onSnapshot,query,orderBy,limit}} from 'https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore.js';
const firebaseConfig={json.dumps(FIREBASE_CONFIG, separators=(',', ':'))};
const app=initializeApp(firebaseConfig);const db=getFirestore(app);
window.lb={{update:async(s,p)=>{if(typeof s!='number'||s<0||s>10000)return;if(typeof p!='string'||!/^[a-zA-Z0-9_]+$/.test(p)||p.length<1||p.length>20)return;try{{await addDoc(collection(db,'scores'),{{score:Math.floor(s),player:p.trim(),timestamp:new Date()}})}}catch(e){{console.warn(e)}}},listen:cb=>{{const q=query(collection(db,'scores'),orderBy('score','desc'),limit(10));return onSnapshot(q,s=>cb(s.docs.map(d=>d.data())),e=>console.error(e))}}}};
</script>
<style>
:root{{--bg:#000814;--neon:#00ff88;--glow:#00ff80;--yellow:#ffff40;--purple:#ff00ff;--glass:rgba(10,25,15,0.18);--font:'Orbitron','Courier New',monospace}}
*{{margin:0;padding:0;box-sizing:border-box}}
body,html{{height:100%;overflow:hidden;background:var(--bg);font-family:var(--font);color:var(--neon)}}
canvas{{display:block}}
.glass{{background:var(--glass);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(0,255,136,0.3);border-radius:12px;padding:16px;box-shadow:0 0 12px rgba(0,255,136,0.5);transition:all .3s;pointer-events:auto}}
.glass:hover{{box-shadow:0 0 20px rgba(0,255,136,0.8);transform:translateY(-1px)}}
#log{{top:16px;left:16px;max-width:520px;font-size:.92em}}
#lb{{bottom:16px;left:16px;max-width:280px}}
#chat{{bottom:16px;right:16px;max-width:280px}}
#score{{top:16px;left:50%;transform:translateX(-50%);font-weight:700;color:var(--yellow);font-size:1.5em;text-shadow:0 0 16px var(--yellow)}}
#vr-status{{top:16px;right:16px;background:rgba(0,255,128,0.2);color:#000;padding:8px 14px;border-radius:8px;font-weight:bold;font-size:.9em}}
#donate-crypto{{bottom:16px;left:50%;transform:translateX(-50%);max-width:320px;text-align:center;font-size:.85em;padding:10px}}
#local-time{{position:fixed;top:16px;right:16px;font-size:.8em;color:var(--yellow);opacity:.8;z-index:999}}
button{{background:rgba(0,15,10,0.4);color:var(--neon);border:1.5px solid var(--neon);padding:10px 22px;margin:6px;border-radius:10px;cursor:pointer;font-weight:600;letter-spacing:1px;transition:all .3s;box-shadow:0 0 10px rgba(0,255,136,0.3)}}
button:hover{{background:var(--neon);color:#000;box-shadow:0 0 25px var(--glow);transform:scale(1.05)}}
#chat-input{{width:68%;background:rgba(0,0,0,0.4);color:var(--neon);border:1px solid var(--purple);padding:8px;border-radius:6px;font-family:var(--font);backdrop-filter:blur(4px)}}
#legal{{position:fixed;bottom:8px;left:50%;transform:translateX(-50%);font-size:.7em;opacity:.7;z-index:999;text-align:center}}
#legal a{{color:#0f0;text-decoration:underline}}
::-webkit-scrollbar{{width:8px}}::-webkit-scrollbar-track{{background:rgba(0,10,5,0.3);border-radius:4px}}::-webkit-scrollbar-thumb{{background:var(--neon);border-radius:4px;box-shadow:0 0 10px var(--neon)}}
</style>
</head>
<body>
<div id="local-time">{LOCAL_TIME}</div>
<div id="log" class="glass" role="log" aria-live="polite"><strong>SLYVERSE v1 — WebXR VR</strong><br><span>WASD (desktop) • Controllers (VR) • Devora • Desbloquea Lore</span><br><br><strong>0RB1T4LSN4K3R,</strong><br>Mr. White cae. Seth asciende en VR.<br><div id="lore-progress" style="margin-top:8px;color:var(--yellow)">LORE: 0/7</div><div id="vr-status" role="status" aria-live="polite">VR: READY</div></div>
<div id="lb" class="glass" role="region" aria-label="Leaderboard"><strong>GLOBAL COILS</strong><div id="lb-list" style="max-height:180px;overflow-y:auto;margin-top:6px">CARGANDO...</div></div>
<div id="chat" class="glass" role="region" aria-label="Chat"><strong>ENTROPY CHAT</strong><div id="chat-list" style="max-height:120px;overflow-y:auto;margin:6px 0"></div><input id="chat-input" placeholder="entropía..." aria-label="Mensaje de chat"><button onclick="sendChat()" aria-label="Enviar">SEND</button></div>
<div id="score" role="status" aria-live="assertive">COILS: 0</div>
<div id="vr-btn-container" style="position:fixed;bottom:80px;left:50%;transform:translateX(-50%);z-index:1000"></div>
<div id="donate-crypto" class="glass"><strong style="color:var(--yellow)">¿Te mola el grid?</strong><br><span>Apoya al dev con crypto (opcional):</span><br><button onclick="copyWallet()" style="margin:6px auto;display:block;font-size:.9em;padding:8px 16px">0x2bd4...2fea</button><div id="donate-qr" style="margin-top:8px;opacity:0"></div><small style="opacity:.7">ETH / MATIC / BASE — 0 fees para ti</small></div>
<div id="legal"><a href="javascript:showPrivacy()">Privacidad</a> • <a href="javascript:showTerms()">Términos</a> • © 2025 0RB1T4L STUDIOS</div>
<script type="module">
const lore=[{{score:50,title:"ENTRY",text:"Mr. White cae. El grid despierta en VR."}},{{score:100,title:"COMPOUND",text:"Tu serpiente crece. Seth observa tus movimientos."}},{{score:200,title:"BOOST",text:"Entropía fluye. VR respira contigo."}},{{score:300,title:"NFT",text:"Tu serpiente VR se graba en SVG eterno."}},{{score:500,title:"METAVERSO",text:"Seth asciende. Mr. White olvidado en el grid."}},{{score:750,title:"YIELD",text:"El ciclo cierra en inmersión."}},{{score:1000,title:"ASCENDIDO",text:"Eres el grid VR. 0rb1t4lsn4k3r reina."}}];
let unlockedLore=0,score=0;
let playerName=localStorage.getItem('slyverse_name')||'guest_'+Math.random().toString(36).substr(2,6);
if(!localStorage.getItem('slyverse_name')){{const n=prompt('Tu alias (1-20 chars, solo letras/números/_):',playerName);if(n&&/^[a-zA-Z0-9_]+$/.test(n)&&n.length<=20){{playerName=n;localStorage.setItem('slyverse_name',n)}}}}
const scoreEl=document.getElementById('score');
import * as THREE from 'three';
import {{VRButton}} from 'three/addons/webxr/VRButton.js';
const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(75,innerWidth/innerHeight,0.1,1000),renderer=new THREE.WebGLRenderer({{antialias:true,alpha:true}});
renderer.setSize(innerWidth,innerHeight);renderer.xr.enabled=true;document.body.appendChild(renderer.domElement);
const vrBtn=VRButton.createButton(renderer);document.getElementById('vr-btn-container').appendChild(vrBtn);
const vrStatus=document.getElementById('vr-status');
if(!renderer.xr.isSupported()){{vrBtn.style.display='none';vrStatus.innerText='VR: NO SOPORTADO'}}
const grid=new THREE.GridHelper(100,100,0x00ff88,0x00ff88);grid.material.opacity=0.15;grid.material.transparent=true;scene.add(grid);
camera.position.set(0,35,60);scene.add(new THREE.AmbientLight(0x00ff88,0.4));
const light=new THREE.PointLight(0x00ff80,1.8);light.position.set(0,30,0);scene.add(light);
const snake=[],headGeo=new THREE.BoxGeometry(1,1,1),headMat=new THREE.MeshBasicMaterial({{color:0x00ff80}});
let head=new THREE.Mesh(headGeo,headMat);head.position.set(0,0.5,0);scene.add(head);snake.push(head);
let food;function spawnFood(){{if(food)scene.remove(food);food=new THREE.Mesh(new THREE.SphereGeometry(0.7,16,16),new THREE.MeshBasicMaterial({{color:0xffff40,emissive:0xffff40,emissiveIntensity:0.6}}));food.position.set(Math.random()*40-20,0.5,Math.random()*40-20);scene.add(food)}}spawnFood();
const keys={{}};let dir={{x:1,z:0}};
window.addEventListener('keydown',e=>keys[e.key.toLowerCase()]=true);
window.addEventListener('keyup',e=>keys[e.key.toLowerCase()]=false);
function beep(f=440,d=100){{const a=new AudioContext(),o=a.createOscillator(),g=a.createGain();o.frequency.value=f;g.gain.setValueAtTime(0.3,a.currentTime);g.gain.exponentialRampToValueAtTime(0.01,a.currentTime+d/1000);o.connect(g);g.connect(a.destination);o.start();o.stop(a.currentTime+d/1000)}}
let breath=0;
function animate(){{breath+=0.012;const s=1+Math.sin(breath)*0.08;grid.scale.set(s,1,s);light.intensity=1.8+Math.sin(breath*3)*0.6;
if(!renderer.xr.isPresenting){{if(keys.w||keys['arrowup'])dir={{x:0,z:-1}};if(keys.s||keys['arrowdown'])dir={{x:0,z:1}};if(keys.a||keys['arrowleft'])dir={{x:-1,z:0}};if(keys.d||keys['arrowright'])dir={{x:1,z:0}}}}
else{{const sess=renderer.xr.getSession();if(sess&&sess.inputSources)for(const src of sess.inputSources)if(src.gamepad&&src.gamepad.axes){{const[x,y]=src.gamepad.axes;if(Math.abs(x)>0.7)dir={{x:Math.sign(x),z:0}};if(Math.abs(y)>0.7)dir={{x:0,z:Math.sign(y)}}}}}}
const p=snake[0].position,nx=p.x+dir.x,nz=p.z+dir.z;
if(Math.abs(nx)>25||Math.abs(nz)>25){{beep(180,400);alert(`GAME OVER: ${{score}} COILS`);reset();return}}
const newHead=new THREE.Mesh(headGeo,headMat);newHead.position.set(nx,0.5,nz);scene.add(newHead);snake.unshift(newHead);
if(food&&Math.abs(nx-food.position.x)<1&&Math.abs(nz-food.position.z)<1){{score+=10;scoreEl.innerText=`COILS: ${{score}}`;beep(880,160);spawnFood();checkLore();if(window.lb)window.lb.update(score,playerName);if(score>=300&&score<310)exportSnakeSVG()}}else scene.remove(snake.pop());
renderer.render(scene,camera)}}renderer.setAnimationLoop(animate);
function reset(){{snake.forEach(s=>scene.remove(s));snake.length=0;head=new THREE.Mesh(headGeo,headMat);head.position.set(0,0.5,0);scene.add(head);snake.push(head);score=0;scoreEl.innerText='COILS: 0';spawnFood()}}
renderer.xr.addEventListener('sessionstart',()=>vrStatus.innerText='VR: ACTIVE');
renderer.xr.addEventListener('sessionend',()=>vrStatus.innerText='VR: READY');
function checkLore(){{lore.forEach((l,i)=>{{if(score>=l.score&&i>=unlockedLore){{unlockedLore++;showLore(l);document.getElementById('lore-progress').innerText=`LORE: ${{unlockedLore}}/7`}}}})}}
function showLore(l){{const m=document.createElement('div');m.style.position='fixed';m.style.top='50%';m.style.left='50%';m.style.transform='translate(-50%,-50%)';m.style.background='rgba(0,8,20,0.9)';m.style.border='2px solid var(--neon)';m.style.padding='24px';m.style.borderRadius='16px';m.style.maxWidth='80%';m.style.zIndex='9999';m.style.fontFamily='var(--font)';m.style.color='var(--neon)';m.innerHTML=`<strong style="font-size:1.4em;color:var(--yellow)">${{l.title}}</strong><br><br>${{l.text}}<br><br><button onclick="this.parentElement.remove()" style="background:var(--neon);color:#000;border:none;padding:10px 20px;border-radius:8px;cursor:pointer;font-weight:600">CERRAR</button>`;document.body.appendChild(m)}}
function exportSnakeSVG(){{let svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="-30 -30 60 60" style="background:#000">`;snake.forEach((s,i)=>{{const[x,z]=[s.position.x,s.position.z];const h=120+(i*5)%240;svg+=`<rect x="${{x-0.5}}" y="${{z-0.5}}" width="1" height="1" fill="hsl(${{h}},100%,50%)"/>`}});svg+=`</svg>`;const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([svg],{{type:'image/svg+xml'}}));a.download=`slyverse_${{playerName}}_${{score}}.svg`;a.click()}}
function sendChat(){{const i=document.getElementById('chat-input'),m=i.value.trim();if(m&&m.length<=100){{const c=document.getElementById('chat-list');c.innerHTML+=`<div style="margin:4px 0;opacity:.9"><strong>${{playerName}}:</strong> ${{m}}</div>`;c.scrollTop=c.scrollHeight;i.value=''}}}}
if(window.lb)window.lb.listen(s=>document.getElementById('lb-list').innerHTML=s.map(p=>`<div style="margin:3px 0">${{p.player}}: <strong>${{p.score}}</strong></div>`).join('')||'<div style="opacity:.6">Sin datos</div>');
window.onresize=()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight)};
document.addEventListener('contextmenu',e=>e.preventDefault());
function copyWallet(){{navigator.clipboard.writeText('{WALLET_ADDRESS}').then(()=>{const b=event.target,old=b.innerText;b.innerText='¡Copiado!';b.style.background='var(--yellow)';b.style.color='#000';setTimeout(()=>{b.innerText=old;b.style.background='';b.style.color=''},1500);const q=document.getElementById('donate-qr');if(!q.innerHTML){q.innerHTML=`<img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data={WALLET_ADDRESS}" alt="QR" style="border-radius:8px;box-shadow:0 0 12px var(--neon)">`;q.style.opacity='1';q.style.transition='opacity .5s'}})}};
if(typeof window.ethereum==='undefined'&&navigator.userAgent.indexOf('Mobile')===-1)document.getElementById('donate-crypto').style.display='none';
function showPrivacy(){{alert('POLÍTICA DE PRIVACIDAD\\n\\nSLYVERSE no recoge datos personales.\\n- Nombre: localStorage\\n- Puntuaciones: públicas\\n- No cookies ni tracking\\n- Firebase: solo scores\\n\\nDerecho a eliminar: contacta al dev.')}}
function showTerms(){{alert('TÉRMINOS DE USO\\n\\n100% gratuito.\\nProhibido: trampas, spam.\\nUso bajo responsabilidad.\\n© 2025 0RB1T4L STUDIOS')}}
</script>
</body>
</html>"""

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(HTML)

subprocess.run(['git', 'add', OUTPUT_FILE], check=False)
subprocess.run(['git', 'commit', '-m', 'Deploy SLYVERSE v1: HTML + modal lore'], check=False)
subprocess.run(['git', 'push'], check=False)

print(f"Deployed: {OUTPUT_FILE}")
print(f"URL: https://orbitalsnaker.github.io/SLYVERSE/{OUTPUT_FILE}")
print(f"Time: {LOCAL_TIME}")
print(f"Wallet: {WALLET_ADDRESS}")
print("\nFirestore Rules:")
print(FIRESTORE_RULES)