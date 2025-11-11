# SLYVERSE v1 — WebXR Snake Grid

**© 2025 0RB1T4L STUDIOS — Sabadell, ES**  
**Dev:** 0RB1T4LSN4K3R  
**X:** [@0rb1t4lsn4k3r](https://x.com/0rb1t4lsn4k3r)

## What is SLYVERSE?

SLYVERSE is a real-time, multiplayer WebXR Snake game packed into a single HTML file. Built with Three.js, Firebase, and WebGL, it runs on desktop, mobile, or VR with no frameworks, no build, and no bloat. Navigate a 30x30 toroidal grid, chase power-ups, export your snake as an SVG NFT, and compete on a global leaderboard. Chat in the entropy stream. Embrace the chaos.

> *"The grid breathes. The serpent awakens. You forget."*

## Features

- Gameplay Modes: Classic (walls kill), Portal (teleport across grid), AI (auto-pathfinding), Chaos (random reversals).
- Controls: WASD, arrow keys, swipe, or VR controllers (WebXR beta).
- Power-Ups: Speed, Ghost, Multi, Invuln—spawn every 10s, last 8s.
- Mechanics: Toroidal grid, Konami code (+3 fragments), teleport/cloak spells, cycle-based time dilation.
- Visuals: WebGL grid with glitch shaders, neon trails, pulsing portals.
- Audio: Web Audio synth for beeps, whispers, and ambient hum.
- Export: SHA-256 soul hash and SVG snake at score ≥100.
- Multiplayer: Firebase-powered global leaderboard and real-time chat (50 messages).
- PWA: Installable, offline-ready (except chat/leaderboard).
- Privacy: Zero tracking, GDPR clean, localStorage for alias only.

## How to Play

1. Open slyverse.html in a browser or visit [demo link] (TBD).
2. Enter an alias (1-20 chars, letters/numbers/_).
3. Move with WASD, arrows, or swipe. Press SPACE to start.
4. Eat purple food to grow. Hit power-ups for effects.
5. Use [1] to teleport (costs 3 fragments), [2] to cloak, [M] to switch modes.
6. Reach score 100 to export your snake as an SVG NFT.
7. Top 10 scores hit the global leaderboard. Chat in the entropy stream.
8. Find the Konami code for a fragment boost.

**Pro Tip**: Survive cycles (time speeds up) and unlock endings like "DRAGON ATE TIME" or "ETERNAL LOOP".

## Tech Stack

- Three.js (0.168.0): WebGL grid, snake shaders, 3D meshes.
- Firebase Firestore: Real-time leaderboard and chat.
- Web Audio: Procedural synth for beeps and whispers.
- PWA: Service worker for offline play.
- No frameworks. No cookies. No analytics.

## Setup & Deploy

### Prerequisites
- A modern browser (Chrome, Firefox, Edge).
- Firebase account for multiplayer (optional, falls back to localStorage).

### Local Play
1. Clone or download this repo.
2. Open slyverse.html in a browser.
3. Play instantly (offline mode, no multiplayer).

### Deploy to GitHub Pages
1. Fork this repo.
2. Commit slyverse.html and manifest.json.
3. Go to Settings > Pages > Source: main branch, Root folder.
4. Enable GitHub Pages. Site goes live in ~60s.

### Firebase Setup
1. Create a Firebase project at console.firebase.google.com.
2. Add a web app, copy the firebaseConfig object.
3. Paste it into slyverse.html (replace your-api-key, etc.).
4. Set up Firestore with provided rules (see slyverse.html comments).
5. Leaderboard and chat sync globally.

## Roadmap (v2 Ideas)
- WebXR hand-tracking and full VR polish.
- Daily challenge mode with unique grids.
- Snake skins (custom SVG layers).
- Weekly leaderboard resets.
- Background synth loop with dynamic BPM.

## Support

SLYVERSE is 100% free, no data collection beyond public scores and chat. Want to fuel the entropy?

**Wallet**: 0x2bd4e0e310436b7ea9944f2edff25b665cea2fea  
ETH/MATIC/BASE, zero fees. QR in-game. No pressure.

## Legal

- License: MIT.
- Data: localStorage for alias, soul hash, and local scores. Delete via browser clear or DM @0rb1t4lsn4k3r on X.
- Credits: Built in one night (and many silent fixes) by 0rb1t4lsn4k3r. Inspired by neon grids, entropy, and the void.

## Contributing

Fork, tweak, PR. Ideas welcome on X (@0rb1t4lsn4k3r). Keep it pure: no frameworks, no bloat. Let the grid breathe.

**Play now**: [demo link] (TBD)  
**Built**: 11 NOV 2025 — 12:37 CET  
**The serpent orbits. Join the chaos.** 🐍🔮