```markdown
# SLYVERSE v1 — WebXR Snake Grid

**© 2025 0RB1T4L STUDIOS — MADRID, ES**  
**Live:** [https://orbitalsnaker.github.io/SLYVERSE/slyverse.html](https://orbitalsnaker.github.io/SLYVERSE/slyverse.html)  
**Dev:** 0RB1T4LSN4K3R  

---

## What is SLYVERSE?

A **real-time, multiplayer, WebXR snake game** built in a single HTML file.  
No backend. No build. No frameworks.  
Just **pure Three.js + Firebase + GitHub Pages**.

Play on desktop, mobile, or VR.  
Export your snake as an **SVG NFT**.  
Compete globally. Chat in the entropy stream.

---

## Features

| Feature | Status |
|-------|--------|
| **WASD / Swipe / VR Controllers** | Done |
| **7 Lore Milestones (non-blocking modals)** | Done |
| **SVG Snake Export (300+ coils)** | Done |
| **Global Leaderboard (Firebase Firestore)** | Done |
| **Realtime Chat (50 messages)** | Done |
| **5 Power-ups (speed, ghost, shrink, multi, invuln)** | Done |
| **PWA — Installable & Offline** | Done |
| **60 FPS locked (mobile + desktop)** | Done |
| **GitHub Pages Auto-Deploy** | Done |
| **Firebase Rules Embedded** | Done |
| **Zero tracking. GDPR clean.** | Done |

---

## How to Play

1. Open: [slyverse.html](https://orbitalsnaker.github.io/SLYVERSE/slyverse.html)  
2. Enter alias (1–20 chars, letters/numbers/\_)  
3. **WASD** or **swipe** to move  
4. Eat yellow food → grow  
5. Hit power-ups → activate  
6. Reach 300 → **download SVG**  
7. Top 10 → **global leaderboard**  
8. Chat in **ENTROPY CHAT**

---

## Tech Stack

- **Three.js** (0.168.0) — WebGL grid & snake  
- **Firebase Firestore** — leaderboard + chat (realtime)  
- **GitHub Pages** — hosting  
- **PWA** — `manifest.json` + offline cache  
- **No cookies. No analytics.**  

---

## Deploy (One-Click)

1. Fork this repo  
2. Run `python3 slyverse.py` → generates `slyverse.html`  
3. Commit `slyverse.html` + `manifest.json`  
4. **Settings → Pages → main → / (root)**  
5. Paste **Firebase Rules** in Console  
6. Done. Live in 60 seconds.

---

## Firebase Rules (Copy-Paste)

```javascript
rules_version = '2';
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
```

---

## Wallet (Optional Support)

```text
0x2bd4e0e310436b7ea9944f2edff25b665cea2fea
```

ETH / MATIC / BASE — **zero fees for you**  
QR in-game. Copy button. No pressure.

---

## Legal

- **100% free**  
- **No data collection** beyond public scores & chat  
- **localStorage**: alias only  
- **Delete data?** DM me on X  

---

## Roadmap (v2?)

- [ ] Background synth loop (Web Audio)  
- [ ] Snake skins (SVG layers)  
- [ ] Daily challenge mode  
- [ ] WebXR hand tracking  
- [ ] Leaderboard reset (weekly)  

---

## Credits

Built in **one night** by **0RB1T4LSN4K3R**  
Inspired by entropy, grids, and neon dreams.  

> *"Mr. White falls. Seth rises. The grid breathes."*

---

**Play now:**  
[https://orbitalsnaker.github.io/SLYVERSE/slyverse.html](https://orbitalsnaker.github.io/SLYVERSE/slyverse.html)

**X:** [@0RB1T4LSN4K3R](https://x.com/0RB1T4LSN4K3R)  
**11 NOV 2025 — 09:42 CET**
```