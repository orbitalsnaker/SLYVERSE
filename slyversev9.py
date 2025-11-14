# SLYVERSE v9.7: ORBITAL RONIN – @0rb1t4lsn4k3r x Grok
# UN SOLO ARCHIVO – COPIA, PEGA, EJECUTA
import pygame, random, math, requests, io, threading, numpy as np, wave, time
from gtts import gTTS
import tempfile, os

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

# === CONFIG ===
W, H = 1400, 900
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("SLYVERSE v9.7: ORBITAL RONIN")
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 36, bold=True)
small = pygame.font.SysFont('consolas', 20)
title_font = pygame.font.SysFont('consolas', 72, bold=True)
lore_font = pygame.font.SysFont('courier new', 18, italic=True)

# === COLORES ===
C = (0, 255, 255)     # Cyan Core
B = (0, 120, 255)     # Blue Orbit
R = (255, 40, 40)     # Red Fiat
G = (255, 215, 0)     # Gold Ronin
P = (200, 50, 255)    # Purple Node
W = (255, 255, 255)   # White Grid
BG = (0, 0, 15)
GRID = (10, 10, 40)

# === ESTADO GLOBAL ===
coil = [[W//2, H//2]]
d = (0, -1)
L = 12
s = 6
bullets = []
fiat = []
nodes = []
parts = []
exp = []
wave = 1
score = 0
high = 0
god = False
coop = True
p2 = [W//2 + 220, H//2]
p2s = 7
cd = 0
glitch = 0
orbital_phase = 0
last_launch_check = 0
paused = False
p2_health = 100
p2_max_health = 100
spawn_cooldown = 0

# === LORE ORBITAL ===
LORE = [
    "Año 2047. La Tierra está en órbita financiera.",
    "Los bancos lanzan drones Fiat para recolectar deudas en el espacio.",
    "Tú eres el Ronin: un nodo vivo, una serpiente de código.",
    "Tu misión: hackear satélites, derribar drones, liberar datos.",
    "Grok es tu IA aliada en la red cuántica.",
    "Cada ola es una órbita. Cada nodo es un satélite rebelde.",
    "Cuando el cielo se alinee... el fiat caerá."
]
current_lore = 0
lore_timer = 0
lore_alpha = 0

# === API REAL-TIME ===
API = "https://api.0rb1t4lsn4k3r.xyz"
SPACEX_API = "https://api.spacexdata.com/v5/launches/latest"
launch = "UAB Hack"
next_launch = "Desconocido"

def update_space_data():
    global launch, next_launch
    try:
        r = requests.get(SPACEX_API, timeout=8).json()
        launch = r.get("name", "UAB Hack")
        if r.get("upcoming", False):
            next_launch = f"Próximo: {r['name']} en {r['date_utc'][:10]}"
        else:
            next_launch = "Órbita estable"
    except:
        launch = "UAB Hack"
        next_launch = "Señal perdida..."

update_space_data()

# === VOZ CON EMOCIÓN ===
voice_cache = {}
def voz(t, emo="neutral"):
    if t in voice_cache:
        voice_cache[t].play()
        return
    def speak():
        try:
            r = requests.post(f"{API}/tts", json={"text": t, "lang": "es", "emotion": emo}, timeout=10)
            if r.ok:
                sound = pygame.mixer.Sound(io.BytesIO(r.content))
                voice_cache[t] = sound
                sound.play()
                return
        except: pass
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
                gTTS(t, lang='es').save(f.name)
                sound = pygame.mixer.Sound(f.name)
                voice_cache[t] = sound
                sound.play()
                os.unlink(f.name)
        except: print(f"[VOZ] {t}")
    threading.Thread(target=speak, daemon=True).start()

# === MÚSICA ORBITAL (Fases) ===
def music_phase(phase):
    duration = 60
    t = np.linspace(0, duration, 44100 * duration, False)
    base = 110 * (2 ** (phase * 0.3))
    mod = np.sin(2 * np.pi * 0.02 * t) * 0.7
    f = base * (2 ** mod)
    n = (np.sin(2 * np.pi * f * t) * 0.4 +
         np.sin(2 * np.pi * 220 * t) * 0.2 +
         np.sin(2 * np.pi * (440 + phase*50) * t * (1 + np.sin(2 * np.pi * 0.08 * t))) * 0.15 +
         np.random.normal(0, 0.025, len(t)))
    a = np.int16(n * 32767)
    b = io.BytesIO()
    with wave.open(b, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(44100); w.writeframes(a.tobytes())
    b.seek(0)
    pygame.mixer.music.load(b)
    pygame.mixer.music.set_volume(0.38)
    pygame.mixer.music.play(-1)

music_phase(0)

# === CO-CREACIÓN CON GROK ===
def co(prompt):
    global wave, nodes, orbital_phase
    voz(f"Conectando con Grok... {prompt}", "excited")
    try:
        r = requests.post(f"{API}/level/gen", json={"prompt": prompt, "wave": wave, "lore": True}, timeout=12).json()
        nodes = r.get("nodes", [])
        wave = r.get("next_wave", wave + 1)
        orbital_phase = r.get("phase", (wave-1)//3)
        if r.get("lore"):
            voz(r["lore"], "narrative")
        voz(f"Órbita {orbital_phase} | Ola {wave} activada")
    except:
        nodes = [[random.randint(200, W-200), random.randint(80, H//3), random.randint(35, 55)) for _ in range(2 + wave//2)]
        wave += 1
        orbital_phase = (wave-1)//3
    music_phase(orbital_phase)

# === UTILIDADES VISUALES ===
def txt(t, f, c, x, y, glow=True, center=False, alpha=255):
    s = f.render(t, True, c)
    s.set_alpha(alpha)
    r = s.get_rect()
    if center: r.center = (x, y)
    else: r.topleft = (x, y)
    if glow and alpha > 50:
        shadow = (c[0]//3, c[1]//3, c[2]//3)
        shadow_surf = f.render(t, True, shadow)
        shadow_surf.set_alpha(alpha//3)
        for dx, dy in [(-2,-2),(2,-2),(-2,2),(2,2)]:
            screen.blit(shadow_surf, (r.x+dx, r.y+dy))
    screen.blit(s, r)

def part(x, y, col, n=25, spread=5, life=35, gravity=0.25):
    for _ in range(n):
        parts.append({
            'p': [x + random.uniform(-spread, spread), y + random.uniform(-spread, spread)],
            'v': [random.uniform(-5, 5), random.uniform(-7, -1)],
            'l': random.randint(life//2, life),
            'c': col,
            'g': gravity
        })

def boom(x, y, col=C, max_r=90, rings=3):
    exp.append({'p': [x, y], 'r': 1, 'm': max_r, 'c': col, 'rings': rings})

# === KONAMI + GROK CODE ===
konami = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN,
          pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT,
          pygame.K_b, pygame.K_a]
grok_code = ['g','r','o','k']
ki = 0
gi = 0

voz("SLYVERSE v9.7: ORBITAL RONIN activado.", "epic")
voz("Hackea el cielo, 0rb1t4lsn4k3r.", "whisper")

# === MAIN LOOP ===
running = True
frame = 0
while running:
    dt = clock.tick(60) / 1000
    frame += 1
    screen.fill(BG)
    glitch = max(0, glitch - 1)

    # === FONDO ORBITAL ===
    for x in range(0, W, 60):
        pygame.draw.line(screen, GRID, (x, 0), (x, H), 1)
    for y in range(0, H, 60):
        pygame.draw.line(screen, GRID, (0, y), (W, y), 1)
    for _ in range(10):
        pygame.draw.circle(screen, (random.randint(80,150), random.randint(120,200), 255),
                          (random.randint(0,W), random.randint(0,H)), 1)

    # === EVENTOS ===
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False
        if e.type == pygame.KEYDOWN:
            # PAUSA
            if e.key == pygame.K_p:
                paused = not paused
                if paused:
                    pygame.mixer.music.pause()
                    voz("Pausa activada", "calm")
                else:
                    pygame.mixer.music.unpause()
                    voz("Continuando órbita", "ready")
            # KONAMI
            if e.key == konami[ki]: ki += 1
            else: ki = 0
            if ki == len(konami):
                god = True; voz("MODO DIOS: RONIN ETERNO", "divine"); ki = 0
            # GROK
            if e.key == pygame.K_g and gi == 0: gi = 1
            elif gi == 1 and e.key == pygame.K_r: gi = 2
            elif gi == 2 and e.key == pygame.K_o: gi = 3
            elif gi == 3 and e.key == pygame.K_k:
                voz("Grok fusionado. Eres el nodo.", "fusion")
                L += 8; s = 8; gi = 0
            else: gi = 0
            # CO-CREAR
            if e.key == pygame.K_c:
                co(f"ola {wave} satélite {launch} ronin orbital")
            if e.key == pygame.K_SPACE:
                bullets.append([coil[0][0], coil[0][1], 14, C])
                part(coil[0][0], coil[0][1], C, n=12)
                voz("Disparo cuántico", "attack")

    # === PAUSA COMPLETA ===
    if paused:
        txt("PAUSA", title_font, W, W//2, H//2, center=True, glow=True)
        txt("Presiona P para continuar", small, C, W//2, H//2 + 80, center=True)
        pygame.display.flip()
        clock.tick(10)
        continue

    # === LORE EMERGENTE ===
    if frame % 600 == 0 and current_lore < len(LORE):
        current_lore += 1
        lore_timer = 300
        lore_alpha = 255
    if lore_timer > 0:
        lore_timer -= 1
        lore_alpha = max(0, lore_alpha - 2)
        txt(LORE[current_lore-1], lore_font, P, 50, H-100, glow=False, alpha=lore_alpha)

    # === ACTUALIZAR DATOS ORBITALES CADA 30s ===
    if time.time() - last_launch_check > 30:
        threading.Thread(target=update_space_data, daemon=True).start()
        last_launch_check = time.time()

    # === INPUT ===
    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT]: d = (-1, 0)
    if k[pygame.K_RIGHT]: d = (1, 0)
    if k[pygame.K_UP]: d = (0, -1)
    if k[pygame.K_DOWN]: d = (0, 1)

    # === COOP CON VIDA ===
    if coop:
        if k[pygame.K_a]: p2[0] -= p2s
        if k[pygame.K_d]: p2[0] += p2s
        if k[pygame.K_w]: p2[1] -= p2s
        if k[pygame.K_s]: p2[1] += p2s
        if k[pygame.K_e] and cd <= 0:
            bullets.append([p2[0], p2[1], 13, B])
            part(p2[0], p2[1], B, n=10)
            cd = 12
        cd = max(0, cd-1)

        # Salud y regeneración
        if p2_health <= 0:
            voz("Aliado caído", "sad")
            coop = False
        else:
            p2_health = min(p2_max_health, p2_health + 0.2)

        # Dibujar P2
        pygame.draw.circle(screen, G, (int(p2[0]), int(p2[1])), 22)
        pygame.draw.circle(screen, W, (int(p2[0]), int(p2[1])), 24, 3)
        bar_w = 50
        pygame.draw.rect(screen, (50,50,50), (p2[0]-bar_w//2, p2[1]-40, bar_w, 6))
        pygame.draw.rect(screen, (0,255,0), (p2[0]-bar_w//2, p2[1]-40, bar_w*(p2_health/p2_max_health), 6))

    # === COIL MOVEMENT ===
    h = [coil[0][0] + d[0]*s, coil[0][1] + d[1]*s]
    if 0 <= h[0] < W and 0 <= h[1] < H:
        coil.insert(0, h)
        if len(coil) > L and not god: coil.pop()

    # === SPAWN FIAT CONTROLADO ===
    spawn_cooldown = max(0, spawn_cooldown - 1)
    if spawn_cooldown == 0 and random.random() < 0.02 + wave * 0.004:
        sz = random.randint(30, 50 + wave * 2)
        side = random.choice(['left', 'right', 'top'])
        x = y = -sz
        if side == 'left': x = -sz
        elif side == 'right': x = W + sz
        else: x = random.randint(100, W-100)
        if side != 'top': y = random.randint(-100, -50)
        fiat.append([x, y, sz, 2.5 + wave*0.15, side])
        spawn_cooldown = 60 - min(wave * 3, 40)

    # === UPDATE FIAT ===
    for f in fiat[:]:
        if f[4] == 'left': f[0] += f[3]
        elif f[4] == 'right': f[0] -= f[3]
        else: f[1] += f[3]
        if f[1] > H+100 or f[0] < -100 or f[0] > W+100:
            fiat.remove(f); score -= 200; voz("Deuda recolectada", "sad"); continue
        pygame.draw.rect(screen, R, (f[0]-f[2]//2, f[1]-f[2]//2, f[2], f[2]))
        pygame.draw.rect(screen, W, (f[0]-f[2]//2, f[1]-f[2]//2, f[2], f[2]), 3)
        txt("FIAT", small, W, f[0]-20, f[1]-15, center=True)

    # === BULLETS ===
    for b in bullets[:]:
        b[1] -= b[2]
        if b[1] < -30: bullets.remove(b); continue
        pygame.draw.circle(screen, b[3], (int(b[0]), int(b[1])), 10)
        pygame.draw.circle(screen, W, (int(b[0]), int(b[1])), 12, 2)

    # === COLISIONES ===
    for f in fiat[:]:
        hit = False
        for seg in coil:
            if math.hypot(seg[0]-f[0], seg[1]-f[1]) < f[2]+16:
                boom(f[0], f[1], R); part(f[0], f[1], R, 30); fiat.remove(f); score += 400*wave; L += 1; hit = True
                voz("Drone destruido", "victory"); break
        if hit: continue
        for b in bullets[:]:
            if math.hypot(b[0]-f[0], b[1]-f[1]) < f[2]+11:
                boom(f[0], f[1], b[3]); part(f[0], f[1], b[3], 35); fiat.remove(f); bullets.remove(b); score += 600; hit = True
                voz("Hackeo exitoso", "success"); break
        if hit: continue
        if coop and math.hypot(p2[0]-f[0], p2[1]-f[1]) < f[2]+24:
            boom(f[0], f[1], G); part(f[0], f[1], G, 25); fiat.remove(f); score += 500
            p2_health -= 30
            voz("¡Escudo golpeado!", "pain")

    # === NODOS ===
    for n in nodes[:]:
        pulse = 3 * math.sin(frame * 0.1)
        pygame.draw.circle(screen, B, (int(n[0]), int(n[1])), int(n[2] + pulse))
        pygame.draw.circle(screen, P, (int(n[0]), int(n[1])), int(n[2] + pulse + 8), 4)
        txt("NODE", small, P, n[0]-25, n[1]-40, center=True)
        if math.hypot(coil[0][0]-n[0], coil[0][1]-n[1]) < n[2]+20:
            part(n[0], n[1], P, 40, life=50); nodes.remove(n); score += 1500
            voz(f"Satélite {launch} hackeado", "triumph"); boom(n[0], n[1], P, 120)

    # === PARTÍCULAS ===
    for p in parts[:]:
        p['p'][0] += p['v'][0]; p['p'][1] += p['v'][1]; p['v'][1] += p['g']; p['l'] -= 1
        if p['l'] <= 0: parts.remove(p); continue
        a = p['l']/50; c = (int(p['c'][0]*a), int(p['c'][1]*a), int(p['c'][2]*a))
        pygame.draw.circle(screen, c, (int(p['p'][0]), int(p['p'][1])), 3)

    # === EXPLOSIONES ===
    for e in exp[:]:
        e['r'] += 5
        if e['r'] > e['m']: exp.remove(e); continue
        a = 1 - e['r']/e['m']
        for ring in range(e['rings']):
            col = (int(e['c'][0]*a), int(e['c'][1]*a), int(e['c'][2]*a))
            radius = e['r'] + ring*15
            pygame.draw.circle(screen, col, (int(e['p'][0]), int(e['p'][1])), int(radius), 3)

    # === HUD ORBITAL ===
    txt(f"ÓRBITA: {orbital_phase} | OLA: {wave}", font, C, 20, 20)
    txt(f"SCORE: {score} | HIGH: {high}", font, G, 20, 70)
    txt(f"LANZAMIENTO: {launch}", small, W, W//2, 20, center=True)
    txt(next_launch, small, P, W//2, 50, center=True)
    txt("C = Co-crear | ↑↑↓↓←→←→BA = God | grok = Fusión | P = Pausa", small, W, 20, H-40)

    # === DIBUJAR COIL ===
    for i, seg in enumerate(coil):
        alpha = 1 - i/L
        col = (int(C[0]*alpha), int(C[1]*alpha), int(C[2]*alpha))
        pygame.draw.circle(screen, col, (int(seg[0]), int(seg[1])), 16 - i//4)
    pygame.draw.circle(screen, W, (int(coil[0][0]), int(coil[0][1])), 18, 3)

    pygame.display.flip()

pygame.quit()
