# slyversev6_unificado.py — TODAS LAS V AYUDAN | v1-v6 UNIDAS | 90% IMPACTO
# "Haz que todas mis v ayuden a esa." — @0rb1t4lsn4k3r
# Todas contribuyen: 70% niños | 20% devs | 10% Norah & Seth
# Ejecuta: python3 slyversev6_unificado.py
# Repo: https://github.com/orbitalsnaker/SLYVERSE

import pygame
import random
import time
import hashlib
import webbrowser
import threading
import json
import os
from web3 import Web3
import RPi.GPIO as GPIO  # Opcional

# === FIRMADO: TODAS LAS V UNIDAS ===
AUTHOR = "@0rb1t4lsn4k3r"
GROK_CHOICE = "70% niños | 20% devs | 10% Norah & Seth"
BUILD_TIME = "2025-11-13 01:00 UTC"
BUILD_HASH = hashlib.sha256(f"{AUTHOR} v1-v6 {BUILD_TIME}".encode()).hexdigest()[:8]
print(f"\n[SLYVERSE v6 UNIFICADO] TODAS LAS V AYUDAN | FIRMADO POR {AUTHOR}")
print(f"[GROK ELIGE] {GROK_CHOICE}")
print(f"[BUILD] {BUILD_TIME} | HASH: {BUILD_HASH}")
print(f"[REPO] https://github.com/orbitalsnaker/SLYVERSE")

# === CONFIGURACIÓN UNIFICADA ===
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 10
SOUL_BURN_RATE = 0.13
CHEESE_GOAL = 13
RICKROLL_SCORE = 696
TARGET_EUR = 1_490_000
KONAMI_CODE = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN,
               pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT,
               pygame.K_b, pygame.K_a]

# === ARCHIVOS UNIFICADOS ===
PROGRESS_FILE = 'slyverse_progress_unificado.json'
DOOR_PIN = 18

# === WALLET ANÓNIMA ===
CAN_LLOBET_WALLET = "0xTuWalletAnónimaReal"  # <<< TU WALLET
print(f"\n[WALLET] {CAN_LLOBET_WALLET} | Todas v suman aquí")

# === POLYGON ===
POLYGON_RPC = 'https://polygon-rpc.com'
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
connected = w3.is_connected()
print(f"[POLYGON] {'Conectado' if connected else 'Simulado'}")

# === PROGRESO UNIFICADO (v1-v6) ===
def load_progress():
    defaults = {
        'total_sly_mined': 0.0,  # De todas v
        'chalet_fund_eur': 0.0,
        'homes_for_kids_eur': 0.0,  # 70%
        'homes_for_devs_eur': 0.0,  # 20%
        'norah_seth_eur': 0.0,      # 10%
        'total_cheeses': 0,         # v2-v3
        'score': 0,
        'rickrolls': 0,             # v5
        'ismael_challenges': 0,     # v6
        'konami_unlocked': False,   # v6
        'v1_tours': 0,              # v1: Tours 3D
        'donations': [],
        'target_chalet': 'Can Llobet + Hogares de todas v',
        'coords': '41.512°N, 2.090°E',
        'door_opened': False,
        'message': f'Todas v ayudan al 90%. — @{AUTHOR}'
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

# === PYGAME ===
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 260))  # HUD para todas v
pygame.display.set_caption(f"SLYVERSE v6 UNIFICADO | €{progress['chalet_fund_eur']:.0f}/1.49M | {BUILD_HASH}")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier', 18, bold=True)
small_font = pygame.font.SysFont('Courier', 14)

# === SERPIENTE (CORE DE TODAS V) ===
snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
direction = (1, 0)
sly_mined = 0.0
cheeses_eaten = progress['total_cheeses']
score = progress['score']
soul_burn_active = True
MODES = ['human', 'ai', 'cultist', 'vr']
CURRENT_MODE = 'cultist'
konami_input = []

def spawn_cheese():
    while True:
        pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        if pos not in snake:
            return pos

cheese = spawn_cheese()

# === PUERTA FÍSICA (v6) ===
def setup_door():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DOOR_PIN, GPIO.OUT)
        GPIO.output(DOOR_PIN, GPIO.LOW)
        print("[PUERTA] Configurada | Todas v abren hogares")
    except:
        print("[PUERTA] Sim")

def open_can_llobet_door():
    if progress['door_opened']: return
    total_fund = progress['chalet_fund_eur'] + progress['homes_for_kids_eur'] + progress['homes_for_devs_eur'] + progress['norah_seth_eur']
    if total_fund >= TARGET_EUR:
        try:
            GPIO.output(DOOR_PIN, GPIO.HIGH)
            time.sleep(10)
            GPIO.output(DOOR_PIN, GPIO.LOW)
            progress['door_opened'] = True
            save_progress(progress)
            print("\nPUERTA ABIERTA | TODAS V CONQUISTAN HOGARES.")
        except:
            print("\nPUERTA ABIERTA (SIM) — LEGADO UNIFICADO.")

setup_door()

# === MINADO UNIFICADO (TODAS V SUMAN) ===
def mine_sly(version='v6'):
    global sly_mined
    if not soul_burn_active: return
    sly_mined += SOUL_BURN_RATE
    progress['total_sly_mined'] += SOUL_BURN_RATE
    if version == 'v1': progress['v1_tours'] += 1  # v1 contribuye
    save_progress(progress)
    if sly_mined >= 1.0:
        sly_mined -= 1.0
        threading.Thread(target=donate_voluntary, daemon=True).start()

def donate_voluntary():
    time.sleep(0.5)
    print("\n" + "="*75)
    print(" $SLY DE TODAS V = IMPACTO | ¿DONAS?")
    print("="*75)
    print(f"Wallet: {CAN_LLOBET_WALLET}")
    print("→ 70% niños | 20% devs | 10% Norah & Seth")
    print("\n1. €0.5 (unificado) | 2. Especifica | 3. Sanar")
    choice = input("Elige: ").strip()
    if choice == "1":
        donate_to_hogares(0.5)
    elif choice == "2":
        try:
            amt = float(input("€: "))
            dest = input("Destino (kids/devs/norah): ").strip().lower()
            donate_to_hogares(amt, dest)
        except: pass

def donate_to_hogares(eur_amount, dest='equilibrado'):
    if dest == 'equilibrado':
        kids_amt = eur_amount * 0.7
        devs_amt = eur_amount * 0.2
        norah_amt = eur_amount * 0.1
        progress['homes_for_kids_eur'] += kids_amt
        progress['homes_for_devs_eur'] += devs_amt
        progress['norah_seth_eur'] += norah_amt
        print(f"[UNIFICADO] +€{kids_amt:.2f} niños | +€{devs_amt:.2f} devs | +€{norah_amt:.2f} familia")
    else:
        if dest == 'kids':
            progress['homes_for_kids_eur'] += eur_amount
            print(f"[NIÑOS] +€{eur_amount} (de todas v)")
        elif dest == 'devs':
            progress['homes_for_devs_eur'] += eur_amount
            print(f"[DEVS] +€{eur_amount} (v4 suma)")
        elif dest == 'norah':
            progress['norah_seth_eur'] += eur_amount
            print(f"[FAMILIA] +€{eur_amount} (10%)")
    
    progress['chalet_fund_eur'] += eur_amount * 0.1
    progress['donations'].append({
        'amount_eur': eur_amount,
        'from_versions': 'v1-v6',
        'dest': dest,
        'timestamp': time.strftime("%Y-%m-%d %H:%M")
    })
    save_progress(progress)
    total_fund = progress['chalet_fund_eur'] + progress['homes_for_kids_eur'] + progress['homes_for_devs_eur'] + progress['norah_seth_eur']
    print(f"Total: €{total_fund:.0f}")
    open_can_llobet_door()
    webbrowser.open(f"https://polygonscan.com/address/{CAN_LLOBET_WALLET}")

# === IA (v4) ===
def ai_move():
    head = snake[0]
    dx, dy = cheese[0] - head[0], cheese[1] - head[1]
    if abs(dx) > abs(dy):
        return (1 if dx > 0 else -1, 0)
    return (0, 1 if dy > 0 else -1)

# === KONAMI + RICKROLL (v5-v6) ===
def check_konami(event_key):
    global konami_input
    konami_input.append(event_key)
    if len(konami_input) > len(KONAMI_CODE):
        konami_input = konami_input[-len(KONAMI_CODE):]
    if konami_input == KONAMI_CODE:
        progress['konami_unlocked'] = True
        save_progress(progress)
        print("\nKONAMI: Todas v despiertan | +€0.5 niños")
        trigger_rickroll()
        konami_input = []

def trigger_rickroll():
    progress['rickrolls'] += 1
    save_progress(progress)
    print("\n696 = RISA | Dona de v5 a devs")
    threading.Thread(target=webbrowser.open, args=("https://www.youtube.com/watch?v=dQw4w9WgXcQ",)).start()
    donate_to_hogares(0.5, 'devs')
    auto_tweet()

# === TWEET + ISMAEL (v6) ===
def auto_tweet():
    tweet = f"#SLYVERSEv6 TodasV | €{progress['homes_for_kids_eur']:.0f} niños | v1-v6 unidas | @{AUTHOR}"
    url = f"https://twitter.com/intent/tweet?text={tweet.replace(' ', '%20')}"
    webbrowser.open(url)

def ismael_challenge():
    progress['ismael_challenges'] += 1
    save_progress(progress)
    print("\nISMAEL: Mañana 11h | Todas v a pie")
    def notify():
        time.sleep(23*3600)
        print("\n¡HORA! v1-v6 conquistan.")
    threading.Thread(target=notify, daemon=True).start()

# === COLORES ===
BLACK = (13, 2, 8)
NEON_GREEN = (57, 255, 20)
COSMIC_PURPLE = (138, 43, 226)
CHEESE_YELLOW = (255, 215, 0)
VR_BLUE = (0, 191, 255)
CAN_LOBLET_GREEN = (0, 100, 0)

# === BUCLE UNIFICADO ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: running = False
            elif event.key == pygame.K_m:
                idx = (MODES.index(CURRENT_MODE) + 1) % len(MODES)
                CURRENT_MODE = MODES[idx]
            elif event.key == pygame.K_d: mine_sly('v6')  # Todas suman
            elif event.key == pygame.K_p: auto_tweet()
            elif event.key == pygame.K_i: ismael_challenge()
            check_konami(event.key)

            if CURRENT_MODE == 'human':
                if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)

    if CURRENT_MODE in ['ai', 'cultist']:
        new_dir = ai_move()
        if (new_dir[0] + direction[0], new_dir[1] + direction[1]) != (0, 0):
            direction = new_dir

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
            progress['total_cheeses'] = cheeses_eaten  # v2-v3 suma
            progress['score'] = score
            mine_sly('v2')  # Todas contribuyen
            cheese = spawn_cheese()
            if score >= RICKROLL_SCORE or progress['konami_unlocked']:
                trigger_rickroll()
                score = 0
        else:
            snake.pop()
        save_progress(progress)

    # === DIBUJO ===
    screen.fill(BLACK)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (20, 20, 30), rect, 1)
    
    for i, seg in enumerate(snake):
        color = VR_BLUE if CURRENT_MODE == 'vr' or progress['konami_unlocked'] else NEON_GREEN
        alpha = max(50, 255 - i * 3)
        s = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(s, (*color, alpha), (CELL_SIZE//2, CELL_SIZE//2), CELL_SIZE//3)
        screen.blit(s, (seg[0]*CELL_SIZE, seg[1]*CELL_SIZE))
    
    pygame.draw.circle(screen, CHEESE_YELLOW, 
                      (cheese[0]*CELL_SIZE + CELL_SIZE//2, cheese[1]*CELL_SIZE + CELL_SIZE//2), 
                      CELL_SIZE//3)
    
    # HUD | TODAS V
    hud_y = WINDOW_SIZE + 10
    pygame.draw.rect(screen, CAN_LOBLET_GREEN, (0, hud_y, WINDOW_SIZE, 250))
    
    progress_bar_w = int((progress['chalet_fund_eur'] / TARGET_EUR) * (WINDOW_SIZE - 40))
    pygame.draw.rect(screen, NEON_GREEN, (20, hud_y + 10, progress_bar_w, 20))
    
    texts = [
        f"$SLY (v1-v6): {sly_mined:.2f} | QUESOS: {cheeses_eaten}/{CHEESE_GOAL} | MODO: {CURRENT_MODE}",
        f"SCORE: {score} | RICKROLLS: {progress['rickrolls']} | KONAMI: {'ON' if progress['konami_unlocked'] else 'OFF'}",
        f"CAN LLOBET: €{progress['chalet_fund_eur']:.0f}/1.490.000",
        f"NIÑOS (70%): €{progress['homes_for_kids_eur']:.0f} | DEVS (20%): €{progress['homes_for_devs_eur']:.0f} | FAMILIA (10%): €{progress['norah_seth_eur']:.0f}",
        f"Tours v1: {progress['v1_tours']} | Wallet: {CAN_LLOBET_WALLET[:10]}... | D=Donar P=Tweet I=Ismael",
        f"{progress['coords']} | Puerta: {'ABIERTA' if progress['door_opened'] else 'CERRADA'}",
        f"FIRMADO POR {AUTHOR} | {progress['message']}"
    ]
    
    for i, text in enumerate(texts):
        color = COSMIC_PURPLE if i == 0 else NEON_GREEN if i == 1 else BLACK
        font_use = font if i < 3 else small_font
        rendered = font_use.render(text, True, color)
        screen.blit(rendered, (20, hud_y + 35 + i*15))
    
    pygame.display.flip()
    clock.tick(FPS)

# === CIERRE UNIFICADO ===
GPIO.cleanup() if 'GPIO' in globals() else None
pygame.quit()
total_fund = progress['chalet_fund_eur'] + progress['homes_for_kids_eur'] + progress['homes_for_devs_eur'] + progress['norah_seth_eur']
print(f"\nSLYVERSE v6 UNIFICADO CERRADO | Total: €{total_fund:.0f} | v1-v6 ayudan")
print(f"Subido: slyversev6_unificado.py + {PROGRESS_FILE}")
print(f"Todas v: 90% impacto. — @{AUTHOR}")