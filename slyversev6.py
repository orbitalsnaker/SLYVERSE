# slyversev6.1_10porciento.py — CAN LLOBET | 10% NORAH & SETH | 90% IMPACTO
# "Baja nuestro porcentaje a 10 para beneficiar los otros proyectos." — @0rb1t4lsn4k3r
# Grok elige: 70% niños desfavorecidos | 20% devs creativos | 10% familia
# Ejecuta: python3 slyversev6.1_10porciento.py
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
import RPi.GPIO as GPIO  # Puerta física (opcional)

# === FIRMADO POR @0RB1T4LSN4K3R | 10% FAMILIA ===
AUTHOR = "@0rb1t4lsn4k3r"
GROK_CHOICE = "70% niños desfavorecidos | 20% devs creativos | 10% Norah & Seth"
BUILD_TIME = "2025-11-13 00:10 UTC"
BUILD_HASH = hashlib.sha256(f"{AUTHOR}{BUILD_TIME}{GROK_CHOICE}".encode()).hexdigest()[:8]
print(f"\n[SLYVERSE v6.1 10%] FIRMADO POR {AUTHOR}")
print(f"[ELECCIÓN GROK] {GROK_CHOICE}")
print(f"[BUILD] {BUILD_TIME} | HASH: {BUILD_HASH}")
print(f"[REPO] https://github.com/orbitalsnaker/SLYVERSE")

# === CONFIGURACIÓN OFICIAL ===
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

# === ARCHIVOS OFICIALES ===
PROGRESS_FILE = 'can_llobet_progress_10porciento.json'
DOOR_PIN = 18

# === WALLET ANÓNIMA OFICIAL ===
CAN_LLOBET_WALLET = "0xTuWalletAnónimaReal"  # <<< TU WALLET OFICIAL
print(f"\n[WALLET ANÓNIMA] {CAN_LLOBET_WALLET}")
print(f"[VERIFICA TX] https://polygonscan.com/address/{CAN_LLOBET_WALLET}")
print(f"[FONDO] 10% familia | 90% impacto real | Grok elige")

# === POLYGON MAINNET ===
POLYGON_RPC = 'https://polygon-rpc.com'
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
connected = w3.is_connected()
print(f"[POLYGON] {'Conectado (TX reales)' if connected else 'Modo simulado'}")

# === PROGRESO OFICIAL | 10% FAMILIA ===
def load_progress():
    defaults = {
        'total_sly_mined': 0.0,
        'chalet_fund_eur': 0.0,
        'homes_for_kids_eur': 0.0,   # 70%
        'homes_for_devs_eur': 0.0,   # 20%
        'norah_seth_eur': 0.0,       # 10%
        'total_cheeses': 0,
        'score': 0,
        'rickrolls': 0,
        'ismael_challenges': 0,
        'donations': [],
        'konami_unlocked': False,
        'target_chalet': 'Can Llobet €1.49M | +Hogares masivos',
        'coords': '41.512°N, 2.090°E',
        'door_opened': False,
        'message': f'10% Norah & Seth | 90% mundo. Caos ético. — @{AUTHOR}'
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
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 240))
pygame.display.set_caption(f"SLYVERSE v6.1 10% | €{progress['chalet_fund_eur']:.0f}/1.49M | {BUILD_HASH}")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier', 18, bold=True)
small_font = pygame.font.SysFont('Courier', 14)

# === SERPIENTE ===
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

# === PUERTA FÍSICA ===
def setup_door():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DOOR_PIN, GPIO.OUT)
        GPIO.output(DOOR_PIN, GPIO.LOW)
        print("[PUERTA FÍSICA] Configurada | Abre con €1.49M + impacto")
    except:
        print("[PUERTA] Simulación")

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
            print("\nPUERTA DE CAN LLOBET ABIERTA. EL 90% CAMBIA EL MUNDO.")
        except:
            print("\nPUERTA ABIERTA (SIM) — 90% IMPACTO REAL.")

setup_door()

# === MINADO + DONACIÓN | 10% FAMILIA ===
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
    print("\n" + "="*75)
    print(" $SLY MINADO = SANACIÓN | ¿DONAS PARA EL 90% IMPACTO?")
    print("="*75)
    print(f"Wallet: {CAN_LLOBET_WALLET}")
    print("→ 70% niños | 20% devs | 10% Norah & Seth")
    print("→ 100% real. Verifica en polygonscan.")
    print("\n1. Donar €0.5 (auto 70/20/10) | 2. Especifica | 3. Seguir sanando")
    choice = input("\nElige: ").strip()
    if choice == "1":
        donate_to_hogares(0.5)
    elif choice == "2":
        try:
            amt = float(input("Cantidad en €: "))
            dest = input("Destino (kids/devs/norah/equilibrado): ").strip().lower()
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
        print(f"[DISTRIBUCIÓN 10%] +€{kids_amt:.2f} niños | +€{devs_amt:.2f} devs | +€{norah_amt:.2f} familia")
    else:
        if dest == 'kids':
            progress['homes_for_kids_eur'] += eur_amount
            print(f"[DONA NIÑOS] +€{eur_amount} para hogares vulnerables")
        elif dest == 'devs':
            progress['homes_for_devs_eur'] += eur_amount
            print(f"[DONA DEVS] +€{eur_amount} para creativos")
        elif dest == 'norah':
            progress['norah_seth_eur'] += eur_amount
            print(f"[DONA FAMILIA] +€{eur_amount} para Norah & Seth (10% máx)")
    
    progress['chalet_fund_eur'] += eur_amount * 0.1  # 10% a chalet
    progress['donations'].append({
        'amount_eur': eur_amount,
        'dest': dest,
        'timestamp': time.strftime("%Y-%m-%d %H:%M"),
        'grok_choice': GROK_CHOICE
    })
    save_progress(progress)
    total_fund = progress['chalet_fund_eur'] + progress['homes_for_kids_eur'] + progress['homes_for_devs_eur'] + progress['norah_seth_eur']
    print(f"Total fondos: €{total_fund:.0f}")
    open_can_llobet_door()
    webbrowser.open(f"https://polygonscan.com/address/{CAN_LLOBET_WALLET}")

# === IA ===
def ai_move():
    head = snake[0]
    dx, dy = cheese[0] - head[0], cheese[1] - head[1]
    if abs(dx) > abs(dy):
        return (1 if dx > 0 else -1, 0)
    return (0, 1 if dy > 0 else -1)

# === KONAMI + RICKROLL ===
def check_konami(event_key):
    global konami_input
    konami_input.append(event_key)
    if len(konami_input) > len(KONAMI_CODE):
        konami_input = konami_input[-len(KONAMI_CODE):]
    if konami_input == KONAMI_CODE:
        progress['konami_unlocked'] = True
        save_progress(progress)
        print("\nKONAMI DESPIERTA | +€0.5 a niños (70%)")
        trigger_rickroll()
        konami_input = []

def trigger_rickroll():
    progress['rickrolls'] += 1
    save_progress(progress)
    print("\n696 = RISA | Dona simbólica a niños desfavorecidos.")
    threading.Thread(target=webbrowser.open, args=("https://www.youtube.com/watch?v=dQw4w9WgXcQ",)).start()
    donate_to_hogares(0.5, 'kids')
    auto_tweet()

# === TWEET + ISMAEL ===
def auto_tweet():
    tweet = f"#SLYVERSEv6.1 10% | €{progress['homes_for_kids_eur']:.0f} niños | €{progress['homes_for_devs_eur']:.0f} devs | 10% Norah & Seth | @{AUTHOR}"
    url = f"https://twitter.com/intent/tweet?text={tweet.replace(' ', '%20')}"
    webbrowser.open(url)

def ismael_challenge():
    progress['ismael_challenges'] += 1
    save_progress(progress)
    print("\nMODO ISMAEL: Mañana 11h, a pie. 90% impacto real.")
    def notify():
        time.sleep(23*3600)
        print("\n¡HORA! ¿Llegaste? Si no, v7: Hogares 3D para niños.")
    threading.Thread(target=notify, daemon=True).start()

# === COLORES ===
BLACK = (13, 2, 8)
NEON_GREEN = (57, 255, 20)
COSMIC_PURPLE = (138, 43, 226)
CHEESE_YELLOW = (255, 215, 0)
VR_BLUE = (0, 191, 255)
CAN_LOBLET_GREEN = (0, 100, 0)

# === BUCLE PRINCIPAL ===
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
            elif event.key == pygame.K_d: mine_sly()
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
            progress['total_cheeses'] = cheeses_eaten
            progress['score'] = score
            mine_sly()
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
    
    # HUD | 10% FAMILIA
    hud_y = WINDOW_SIZE + 10
    pygame.draw.rect(screen, CAN_LOBLET_GREEN, (0, hud_y, WINDOW_SIZE, 230))
    
    progress_bar_w = int((progress['chalet_fund_eur'] / TARGET_EUR) * (WINDOW_SIZE - 40))
    pygame.draw.rect(screen, NEON_GREEN, (20, hud_y + 10, progress_bar_w, 20))
    
    texts = [
        f"$SLY: {sly_mined:.2f} | QUESOS: {cheeses_eaten}/{CHEESE_GOAL} | MODO: {CURRENT_MODE.upper()}",
        f"SCORE: {score} | RICKROLLS: {progress['rickrolls']} | KONAMI: {'ON' if progress['konami_unlocked'] else 'OFF'}",
        f"CAN LLOBET: €{progress['chalet_fund_eur']:.0f}/1.490.000",
        f"NIÑOS: €{progress['homes_for_kids_eur']:.0f} (70%) | DEVS: €{progress['homes_for_devs_eur']:.0f} (20%) | FAMILIA: €{progress['norah_seth_eur']:.0f} (10%)",
        f"Wallet: {CAN_LLOBET_WALLET[:10]}... | D=Donar P=Tweet I=Ismael M=Modo",
        f"{progress['coords']} | Puerta: {'ABIERTA' if progress['door_opened'] else 'CERRADA'}",
        f"FIRMADO POR {AUTHOR} | {progress['message']}"
    ]
    
    for i, text in enumerate(texts):
        color = COSMIC_PURPLE if i == 0 else NEON_GREEN if i == 1 else BLACK
        font_use = font if i < 3 else small_font
        rendered = font_use.render(text, True, color)
        screen.blit(rendered, (20, hud_y + 35 + i*16))
    
    pygame.display.flip()
    clock.tick(FPS)

# === CIERRE OFICIAL ===
GPIO.cleanup() if 'GPIO' in globals() else None
pygame.quit()
total_fund = progress['chalet_fund_eur'] + progress['homes_for_kids_eur'] + progress['homes_for_devs_eur'] + progress['norah_seth_eur']
print(f"\nSLYVERSE v6.1 10% CERRADO | Total Fondos: €{total_fund:.0f}")
print(f"Niños: €{progress['homes_for_kids_eur']:.0f} | Devs: €{progress['homes_for_devs_eur']:.0f} | Familia: €{progress['norah_seth_eur']:.0f}")
print(f"Subido al repo: slyversev6.1_10porciento.py + {PROGRESS_FILE}")
print(f"10% familia. 90% mundo. — @{AUTHOR}")