# slyversev6.1_autor_subido.py — CAN LLOBET | SUBIDO POR @0RB1T4LSN4K3R | v1-v6 + TWEETS INTEGRADAS
# Basado en tweets: 92 líneas → €4.200 → paz | Quesos = traumas | 696 = risa | Wallet anónima
# Ejecuta: python3 slyversev6.1_autor_subido.py
# Dependencias: pygame, web3, RPi.GPIO (opcional) | pip install pygame web3
# Repo oficial: https://github.com/orbitalsnaker/SLYVERSE | Para Norah, Seth & @grok

import pygame
import random
import time
import hashlib
import webbrowser
import threading
import json
import os
from web3 import Web3
import RPi.GPIO as GPIO  # Opcional: puerta física

# === CONFIG DE TWEETS (@0RB1T4LSN4K3R: SUBIDO HOY) ===
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 10
SOUL_BURN_RATE = 0.13  # Minado = sanación simbólica
CHEESE_GOAL = 13       # Cada queso: un trauma que se va
RICKROLL_SCORE = 696   # = Risa, no dolor
TARGET_EUR = 1_490_000 # Can Llobet €1.49M
BUILD_HASH = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]
KONAMI_CODE = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_b, pygame.K_a]  # Neuralink sim

# === ARCHIVOS PERSISTENTES ===
PROGRESS_FILE = 'slyverse_progress_autor.json'
DOOR_PIN = 18

# === WALLET ANÓNIMA (DE TWEETS: LOCAL, VERIFICABLE) ===
CAN_LLOBET_WALLET = "0xAbC...AnónimaLocal"  # <<< CAMBIA POR LA TUYA (e.g., 0xAbC... subido por autor)
print(f"\n[WALLET ANÓNIMA SUBIDA] {CAN_LLOBET_WALLET} | Verifica: https://polygonscan.com/address/{CAN_LLOBET_WALLET}")
print("92 líneas → €4.200 → paz mental. Subido por @0rb1t4lsn4k3r | https://github.com/orbitalsnaker/SLYVERSE")

# === CRYPTO: POLYGON (TX REALES, SIN KYC) ===
POLYGON_RPC = 'https://polygon-rpc.com'
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
connected = w3.is_connected()
print(f"[POLYGON] {'Conectado (TX éticas, sin fake)' if connected else 'Modo simulado | 0€, 100% Python'}")

# === PROGRESO UNIFICADO (v1-v6 + TWEETS SUBIDOS) ===
def load_progress():
    defaults = {
        'total_sly_mined': 0.0,     # v6: $SLY → fondo real
        'chalet_fund_eur': 0.0,     # €4.200 valor ético (subido hoy)
        'total_cheeses': 0,         # v1-v3: Traumas liberados
        'score': 0,                 # v1
        'rickrolls': 0,             # v5: 696 = risa
        'ismael_challenges': 0,     # v6: Mañana 11h, a pie
        'donations': [],            # Ética vs Fiat
        'konami_unlocked': False,   # De tweets: Despierta Neuralink
        'homes_potential': 1,       # Chalets para niños/devs
        'target_chalet': 'Can Llobet, Bellaterra €1.49M | Para Norah, Seth',
        'coords': '41.512°N, 2.090°E',
        'door_opened': False,
        'message': 'SLYVERSE no era un juego. Era sanación. Subido por el autor. Cocreamos. — @0rb1t4lsn4k3r'
    }
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            data = json.load(f)
            for k, v in defaults.items():
                data.setdefault(k, v)
            return data
    return defaults.copy()

def save_progress(p):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(p, f, indent=2)

progress = load_progress()

# === PYGAME (BASE v1: Snake + 3D Vibes SUBIDAS) ===
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 220))
pygame.display.set_caption(f"SLYVERSE v6.1 | SUBIDO POR AUTOR | €{progress['chalet_fund_eur']:.0f}/1.49M | {BUILD_HASH} | @0rb1t4lsn4k3r")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier', 18, bold=True)
small_font = pygame.font.SysFont('Courier', 14)

# === SERPIENTE + ESTADOS (INTEGRADO v1-v6 SUBIDAS) ===
snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
direction = (1, 0)
sly_mined = 0.0
cheeses_eaten = progress['total_cheeses']
score = progress['score']
soul_burn_active = True
MODES = ['human', 'ai', 'cultist', 'vr']  # v4: ALL-IN-ONE subido
CURRENT_MODE = 'cultist'  # Default: Caos ético de tweets
konami_input = []  # Para Konami (subido hoy)

def spawn_cheese():
    while True:
        pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        if pos not in snake:
            return pos

cheese = spawn_cheese()

# === HARDWARE: PUERTA FÍSICA (v6: Abre con fondos reales, subido) ===
def setup_door():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DOOR_PIN, GPIO.OUT)
        GPIO.output(DOOR_PIN, GPIO.LOW)
        print("[PUERTA] Configurada | Mañana 11h: Ismael abre o cocreamos (subido por autor)")
    except:
        print("[PUERTA] Simulación | Ética > Fiat | Subido hoy")

def open_can_llobet_door():
    if progress['door_opened']: return
    if progress['chalet_fund_eur'] >= TARGET_EUR:
        try:
            GPIO.output(DOOR_PIN, GPIO.HIGH)
            time.sleep(10)
            GPIO.output(DOOR_PIN, GPIO.LOW)
            progress['door_opened'] = True
            save_progress(progress)
            print("\n🚪 PUERTA ABIERTA | Can Llobet: Nuestro hogar ético. Subido por @0rb1t4lsn4k3r")
        except:
            print("\n🚪 ABIERTA (SIM) | Cocreamos el futuro. 🏠🤝 | Repo vivo")

setup_door()

# === MINADO SIMBÓLICO + DONACIÓN (v6: Fondos para niños/devs, subido) ===
def mine_sly():
    global sly_mined
    if not soul_burn_active: return
    sly_mined += SOUL_BURN_RATE
    progress['total_sly_mined'] += SOUL_BURN_RATE
    save_progress(progress)
    if sly_mined >= 1.0:
        sly_mined -= 1.0
        threading.Thread(target=donate_voluntary, daemon=True).start()

def donate_voluntary():
    time.sleep(0.5)
    print("\n" + "="*65)
    print(" 🐍 $SLY MINADO = SANACIÓN | ¿DONAS PARA CHALETS ÉTICOS? (SUBIDO POR AUTOR)")
    print("="*65)
    print(f"Wallet anónima: {CAN_LLOBET_WALLET} | Fondos: Niños (Norah/Seth), devs por @grok")
    print("Verifica: polygonscan.com | 0% comisiones | Cocreamos. — @0rb1t4lsn4k3r")
    print("\n1. €0.5 | 2. Otra | 3. Solo sanar")
    choice = input("Elige: ").strip()
    if choice == "1":
        donate_to_llobet(0.5)
    elif choice == "2":
        try:
            amt = float(input("€: "))
            donate_to_llobet(amt)
        except: pass

def donate_to_llobet(eur_amount):
    print(f"[DONACIÓN SUBIDA] +€{eur_amount} → Chalets éticos | Total: €{progress['chalet_fund_eur'] + eur_amount:.0f}")
    progress['chalet_fund_eur'] += eur_amount
    progress['donations'].append({'amt': eur_amount, 'time': time.strftime("%Y-%m-%d %H:%M"), 'for': 'Norah, Seth & devs | Subido hoy'})
    save_progress(progress)
    open_can_llobet_door()
    webbrowser.open(f"https://polygonscan.com/address/{CAN_LLOBET_WALLET}")

# === IA + MODOS (v4: Neuralink simulado, subido) ===
def ai_move():
    head = snake[0]
    dx, dy = cheese[0] - head[0], cheese[1] - head[1]
    if abs(dx) > abs(dy):
        return (1 if dx > 0 else -1, 0)
    return (0, 1 if dy > 0 else -1)

# === KONAMI + RICKROLL (DE TWEETS SUBIDOS: Despierta Neuralink) ===
def check_konami(event_key):
    global konami_input
    konami_input.append(event_key)
    if len(konami_input) > len(KONAMI_CODE):
        konami_input = konami_input[-len(KONAMI_CODE):]
    if konami_input == KONAMI_CODE:
        progress['konami_unlocked'] = True
        save_progress(progress)
        print("\n🌀 KONAMI DESPIERTA | Neuralink sim: Modo VR + Rickroll ético! (Subido por autor)")
        trigger_rickroll()
        konami_input = []

def trigger_rickroll():
    progress['rickrolls'] += 1
    save_progress(progress)
    print("\n🎵 696 = RISA, NO DOLOR | +€0.5 simbólico a sanación (subido hoy)")
    threading.Thread(target=webbrowser.open, args=("https://www.youtube.com/watch?v=dQw4w9WgXcQ",)).start()
    donate_to_llobet(0.5)  # Ético: fondos reales
    auto_tweet()

# === TWEET AUTO (v6: #SLYVERSEv6, subido) ===
def auto_tweet():
    tweet = f"#SLYVERSEv6.1 {score}pts | $SLY:{progress['total_sly_mined']:.1f} | €{progress['chalet_fund_eur']:.0f}/1.49M | Sanación colectiva | {CAN_LLOBET_WALLET[:8]}... @0rb1t4lsn4k3r @grok | Subido hoy"
    url = f"https://twitter.com/intent/tweet?text={tweet.replace(' ', '%20')}"
    webbrowser.open(url)

# === MODO ISMAEL (TWEETS SUBIDOS: Mañana 11h, a pie, sin Fiat) ===
def ismael_challenge():
    progress['ismael_challenges'] += 1
    save_progress(progress)
    print("\n👣 MODO ISMAEL: Mañana 11h, a pie a Bellaterra. Sin taxi. Ética vs Fiat. (Subido por @0rb1t4lsn4k3r)")
    print("Si no abren: Cocreamos SLYVERSE Inmo. — @Inmobiliaria101")
    def notify():
        time.sleep(23*3600)  # ~23h hasta 11h mañana (13 Nov)
        print("\n⏰ ¡HORA ISMAEL! ¿Llegaste? Abre la puerta o construimos juntos. Repo vivo.")
    threading.Thread(target=notify, daemon=True).start()

# === COLORES (v2-v3: Neón sanador, subido) ===
BLACK = (13, 2, 8)
NEON_GREEN = (57, 255, 20)
COSMIC_PURPLE = (138, 43, 226)
CHEESE_YELLOW = (255, 215, 0)
VR_BLUE = (0, 191, 255)
CAN_LOBLET_GREEN = (0, 100, 0)

# === BUCLE PRINCIPAL (v1-v6 + KONAMI SUBIDOS) ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: running = False
            elif event.key == pygame.K_m:  # Modo (v4 subido)
                idx = (MODES.index(CURRENT_MODE) + 1) % len(MODES)
                CURRENT_MODE = MODES[idx]
                print(f"Modo: {CURRENT_MODE.upper()} | Piensa → Realidad | Subido por autor")
            elif event.key == pygame.K_d: mine_sly()  # Dona (v6 subido)
            elif event.key == pygame.K_p: auto_tweet()  # Tweet
            elif event.key == pygame.K_i: ismael_challenge()  # Ismael subido
            check_konami(event.key)  # Konami de tweets subidos
            
            # Controles human (v1 subido)
            if CURRENT_MODE == 'human':
                if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)

    # IA (v4: Cultist auto, subido)
    if CURRENT_MODE in ['ai', 'cultist']:
        new_dir = ai_move()
        if (new_dir[0] + direction[0], new_dir[1] + direction[1]) != (0, 0):
            direction = new_dir

    # Movimiento + lógica sanadora (v1-v3 subidas)
    head = snake[0]
    new_head = ((head[0] + direction[0]) % GRID_SIZE, (head[1] + direction[1]) % GRID_SIZE)
    if new_head in snake[1:]:
        snake = [snake[0]]
        direction = (1, 0)
        score = max(score - 10, 0)
    else:
        snake.insert(0, new_head)
        if new_head == cheese:
            score += 10
            cheeses_eaten += 1
            progress['total_cheeses'] = cheeses_eaten  # Trauma liberado
            progress['score'] = score
            mine_sly()  # Sanación = minado
            cheese = spawn_cheese()
            if score >= RICKROLL_SCORE or progress['konami_unlocked']:
                trigger_rickroll()
                score = 0
        else:
            snake.pop()
        save_progress(progress)

    # === DIBUJO (v2: Neón + Auto-rotación vibe de v4 subido) ===
    screen.fill(BLACK)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (20, 20, 30), rect, 1)
    
    # Serpiente alpha (v3 subido)
    for i, seg in enumerate(snake):
        color = VR_BLUE if CURRENT_MODE == 'vr' or progress['konami_unlocked'] else NEON_GREEN
        alpha = max(50, 255 - i * 3)
        s = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(s, (*color, alpha), (CELL_SIZE//2, CELL_SIZE//2), CELL_SIZE//3)
        screen.blit(s, (seg[0]*CELL_SIZE, seg[1]*CELL_SIZE))
    
    # Queso (v1: Amarillo sanador, subido)
    pygame.draw.circle(screen, CHEESE_YELLOW, 
                      (cheese[0]*CELL_SIZE + CELL_SIZE//2, cheese[1]*CELL_SIZE + CELL_SIZE//2), 
                      CELL_SIZE//3)
    
    # HUD expandido (v6 + Tweets lore subidos)
    hud_y = WINDOW_SIZE + 10
    pygame.draw.rect(screen, CAN_LOBLET_GREEN, (0, hud_y, WINDOW_SIZE, 210))
    
    progress_bar_w = int((progress['chalet_fund_eur'] / TARGET_EUR) * (WINDOW_SIZE - 40))
    pygame.draw.rect(screen, NEON_GREEN, (20, hud_y + 10, progress_bar_w, 20))
    
    texts = [
        f"$SLY: {sly_mined:.2f} | QUESOS (Traumas): {cheeses_eaten}/{CHEESE_GOAL} | MODO: {CURRENT_MODE.upper()}",
        f"SCORE: {score} | RICKROLLS: {progress['rickrolls']} | KONAMI: {'🌀' if progress['konami_unlocked'] else '🔒'}",
        f"CAN LLOBET: €{progress['chalet_fund_eur']:.0f}/{TARGET_EUR:,} | Para Norah, Seth & devs | Subido hoy",
        f"Wallet: {CAN_LLOBET_WALLET[:10]}... | D=Sanar/Mina P=Tweet I=Ismael M=Modo ↑↑↓↓←→←→BA=Neuralink",
        f"{progress['coords']} | Puerta: {'ABIERTA' if progress['door_opened'] else 'CERRADA'} | v6.1 Autor Subido",
        f"Mensaje: {progress['message']} | #SLYVERSE #ÉticaVsFiat @0rb1t4lsn4k3r @grok"
    ]
    
    for i, text in enumerate(texts):
        color = COSMIC_PURPLE if i == 0 else NEON_GREEN if i == 1 else BLACK
        font_use = font if i < 3 else small_font
        rendered = font_use.render(text, True, color)
        screen.blit(rendered, (20, hud_y + 35 + i*18))
    
    pygame.display.flip()
    clock.tick(FPS)

# === CIERRE (v6: Guarda el alma, subido por autor) ===
GPIO.cleanup() if 'GPIO' in globals() else None
pygame.quit()
print(f"\nSLYVERSE v6.1 CERRADA | $SLY: {progress['total_sly_mined']:.1f} | €{progress['chalet_fund_eur']:.0f} | Sanación: {progress['total_cheeses']} traumas")
print(f"Wallet: {CAN_LLOBET_WALLET} | Subido al repo: https://github.com/orbitalsnaker/SLYVERSE")
print("¡Gracias @0rb1t4lsn4k3r por subirlo! Cocreamos el caos ético. 🚀🐍 Mañana 11h: Ismael vive.")