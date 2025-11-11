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
    match /chat/{doc} {
      allow read: if true;
      allow create: if request.auth == null
                  && request.resource.data.keys().hasOnly(['msg','player','time'])
                  && request.resource.data.msg is string
                  && request.resource.data.msg.size() <= 100
                  && request.resource.data.player is string
                  && request.resource.data.player.size() <= 20
                  && request.resource.data.time is timestamp;
      allow delete: if false;
    }
  }
}
"""

HTML = f"""<!DOCTYPE html>
<html lang="es" manifest="slyverse.appcache">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="theme-color" content="#000814"/>
<meta name="author" content="0RB1T4LSN4K3R"/>
<meta name="copyright" content="© 2025 0RB1T4L STUDIOS — MADRID"/>
<meta name="description" content="SLYVERSE v1 – Snake WebXR VR con power-ups, chat global, PWA y SVG NFT. 100% gratis y legal en España."/>
<link rel="manifest" href="manifest.json"/>
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐍</text></svg>"/>
<title>SLYVERSE v1 — WebXR VR</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
<script type="importmap">{{"imports":{{"three":"https://cdn.jsdelivr.net/npm/three@0.168.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.168.0/examples/jsm/"}}}}</script>
<script type="module">
import {{initializeApp}} from 'https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js';
import {{getFirestore,collection,addDoc,onSnapshot,query,orderBy,limit,serverTimestamp}} from 'https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore.js';
const firebaseConfig={json.dumps(FIREBASE_CONFIG, separators=(',', ':'))};
const app=initializeApp(firebaseConfig);const db=getFirestore(app);
window.lb={{update:async(s,p)=>{if(typeof s!='number'||s<0||s>10000)return;if(typeof p!='string'||!/^[a-zA-Z0-9_]+$/.test(p)||p.length<1||p.length>20)return;try{{await addDoc(collection(db,'scores'),{{score:Math.floor(s),player:p.trim(),timestamp:serverTimestamp()}})}}catch(e){{console.warn(e)}}},listen:cb=>{{const q=query(collection(db,'scores'),orderBy('score','desc'),limit(10));return onSnapshot(q,s=>cb(s.docs.map(d=>d.data())),e=>console.error(e))}}}};
window.chat={{send:async(m,p)=>{if(typeof m!='string'||m.length>100||m.length<1)return;try{{await addDoc(collection(db,'chat'),{{msg:m.trim(),player:p,time:serverTimestamp()}})}}catch(e){{console.warn(e)}}},listen:cb=>{{const q=query(collection(db,'chat'),orderBy('time','desc'),limit(50));return onSnapshot(q,s=>cb(s.docs.map(d=>d.data()).reverse()),e=>console.error(e))}}}};
</script>
<style>
:root{{--bg:#000814;--neon:#00ff88;--glow:#00ff80;--yellow:#ffff40;--purple:#ff00ff;--glass:rgba(10,25,15,0.18);--font:'Orbitron','Courier New',monospace}}
*{{margin:0;padding:0;box-sizing:border-box}}
body,html{{height:100%;overflow:hidden;background:var(--bg);font-family:var(--font);color:var(--neon);touch-action:none}}
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
#powerup{{position:fixed;top:60px;left:50%;transform:translateX(-50%);background:rgba(255,0,255,0.2);color:#fff;padding:6px 12px;border-radius:8px;font-size:.8em;z-index:1000;opacity:0;transition:opacity .3s}}
button{{background:rgba(0,15,10,0.4);color:var(--neon);border:1.5px solid var(--neon);padding:10px 22px;margin:6px;border-radius:10px;cursor:pointer;font-weight:600;letter-spacing:1px;transition:all .3s;box-shadow:0 0 10px rgba(0,255,136,0.3)}}
button:hover{{background:var(--neon);color:#000;box-shadow:0 0 25px var(--glow);transform:scale(1.05)}}
#chat-input{{width:68%;background:rgba(0,0,0,0.4);color:var(--neon);border:1px solid var(--purple);padding:8px;border-radius:6px;font-family:var(--font);backdrop-filter:blur(4px)}}
#legal{{position:fixed;bottom:8px;left:50%;transform:translateX(-50%);font-size:.7em;opacity:.7;z-index:999;text-align:center}}
#legal a{{color:#0f0;text-decoration:underline}}
::-webkit-scrollbar{{width:8px}}::-webkit-scrollbar-track{{background:rgba(0,10,5,0.3);border-radius:4px}}::-webkit-scrollbar-thumb{{background:var(--neon);border-radius:4px;box-shadow:0 0 10px var(--neon)}}
</style>
</head>
<body>
<audio id="bgm" loop src="data:audio/midi;base64,TVRoZAAAAAYAAQACA8BNVHJrAAAACwD/UQMIMjYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/UQMIMzYAwAAA/+MASgD/U