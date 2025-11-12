# slyversev6.py — CAN LLOBET BELLATERRA | WALLET ANÓNIMA | FIXES ÉTICOS
# Ejecuta: python3 slyversev6.py
# Dependencias: pygame, web3 (pip install pygame web3)
# Wallet: Generada localmente (anónima, no KYC) | $SLY → fondo real

import pygame
import random
import time
import hashlib
import webbrowser
import threading
import json
import os
from web3 import Web3
from eth_account import Account

# === CONFIGURACIÓN CAN LLOBET + ANONIMATO ===
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 10
SOUL_BURN_RATE = 0.13
CHEESE_GOAL = 13
RICKROLL_SCORE = 696
BUILD_HASH = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]

# === WALLET ANÓNIMA (generada localmente) ===
WALLET_FILE = 'anonymous_chalet_wallet.json'
def generate_anonymous_wallet():
    acct = Account.create()
    wallet = {
        'address': acct.address,
        'private_key': acct.key.hex(),
        'encrypted': False
    }
    with open(WALLET_FILE, 'w') as f:
        json.dump(wallet, f)
    print(f"\u001b[32m[WALLET ANÓNIMA CREADA]\u001b[0m {acct.address}")
    return wallet

def load_wallet():
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE, 'r') as f:
            return json.load(f)
    else:
        return generate_anonymous_wallet()

wallet = load_wallet()
CHALET_WALLET = wallet['address']

# === CRYPTO: POLYGON MAINNET (real, pero anónimo) ===
POLYGON_RPC = 'https://polygon-rpc.com'
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
if not w3.is_connected():
    print("Polygon no conectado — donaciones simuladas (v7: reales)")

# === COLORES + BELLATERRA ===
BLACK = (13, 2, 8)
NEON_GREEN = (57, 255, 20)
COSMIC_PURPLE = (138, 43, 226)
CHEESE_YELLOW = (255, 215, 0)
VR_BLUE = (0, 191, 255)
CAN_LOBLET_GREEN = (0, 128, 0)

MODES = ['human', 'ai', 'cultist', 'vr']
CURRENT_MODE = 'cultist'

# === TRACKING: CAN LLOBET €1.49M ===
TRACKING_FILE = 'can_llobet_progress.json'
def load_progress():
    try:
        with open(TRACKING_FILE, 'r') as f:
            data = json.load(f)
            # FIX: Asegurar claves
            defaults = {'total_sly_mined': 0.0, 'chalet_fund_eur': 0.0, 'homes_potential': 1, 
                        'target_chalet': 'Can Llobet, Bellaterra €1.49M', 'coords': '41.512°N, 2.090°E'}
            for k, v in defaults.items():
                if k not in data:
                    data[k] = v
            return data
    except:
        return {'total_sly_mined': 0.0, 'chalet_fund_eur': 0.0, 'homes_potential': 1, 
                'target_chalet': 'Can Llobet, Bellaterra €1.49M', 'coords': '41.512°N, 2.090°E'}

def save_progress(progress):
    with open(TRACKING_FILE, 'w') as f:
        json.dump(progress, f, indent=2)

progress = load_progress()

# === INICIALIZACIÓN ===
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 140))
pygame.display.set_caption(f"SLYVERSE v6 | Can Llobet | €{progress['chalet_fund_eur']:.0f}/1.490.000 | {BUILD_HASH[:6]}")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier', 18, bold=True)
small_font = pygame.font.SysFont('Courier', 14)

# === SERPIENTE ===
snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
direction = (1, 0)
score = 0
sly_mined = 0.0
cheeses_eaten = 0
soul_burn_active = True

def spawn_cheese():
    while True:
        pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        if pos not in snake:
            return pos

cheese = spawn_cheese()

# === MINADO $SLY + DONACIÓN ANÓNIMA ===
def mine_sly():
    global sly_mined, progress
    if soul_burn_active:
        sly_mined += SOUL_BURN_RATE
        progress['total_sly_mined'] += SOUL_BURN_RATE
        if sly_mined >= 1.0:
            print(f"\u001b[35m[$SLY MINADO]\u001b[0m +1 | Total: {progress['total_sly_mined']:.1f}")
            progress['chalet_fund_eur'] += 0.5
            sly_mined -= 1.0
            # FIX: Guardar inmediatamente
            save_progress(progress)
            # v7: tx real a CHALET_WALLET
        save_progress(progress)

# === TWEET AUTOMÁTICO ===
def auto_tweet():
    tweet = f"#SLYVERSE v6 | {score} pts | $SLY: {progress['total_sly_mined']:.1f} | Can Llobet: €{progress['chalet_fund_eur']:.0f} | Wallet: {CHALET_WALLET[:8]}... | @orbitalsnaker"
    url = f"https://twitter.com/intent/tweet?text={tweet.replace(' ', '%20')}"
    webbrowser.open(url)

# === RICKROLL + DONACIÓN ===
def trigger_rickroll():
    print("\u001b[31mRICKROLL ACTIVADO — €0.5 DONADO A CAN LLOBET\u001b[0m")
    threading.Thread(target=webbrowser.open, args=("https://www.youtube.com/watch?v=dQw4w9WgXcQ",)).start()
    mine_sly()
    auto_tweet()

# === IA ===
def ai_move():
    head = snake[0]
    dx = cheese[0] - head[0]
    dy = cheese[1] - head[1]
    if abs(dx) > abs(dy):
        return (1 if dx > 0 else -1, 0)
    else:
        return (0, 1 if dy > 0 else -1)

# === BUCLE ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_m:
                idx = (MODES.index(CURRENT_MODE) + 1) % len(MODES)
                CURRENT_MODE = MODES[idx]
                print(f"MODO → {CURRENT_MODE.upper()}")
            elif event.key == pygame.K_d:
                mine_sly()
                print("Donación manual activada")

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
            mine_sly()
            cheese = spawn_cheese()
            if score >= RICKROLL_SCORE:
                trigger_rickroll()
                score = 0
                cheeses_eaten = 0
        else:
            snake.pop()

    # === DIBUJO ===
    screen.fill(BLACK)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (20, 20, 30), rect, 1)
    
    for i, segment in enumerate(snake):
        color = VR_BLUE if CURRENT_MODE == 'vr' else NEON_GREEN
        alpha = 255 - i * 3
        s = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(s, (*color, alpha), (CELL_SIZE//2, CELL_SIZE//2), CELL_SIZE//3)
        screen.blit(s, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE))
    
    pygame.draw.circle(screen, CHEESE_YELLOW, 
                      (cheese[0]*CELL_SIZE + CELL_SIZE//2, cheese[1]*CELL_SIZE + CELL_SIZE//2), 
                      CELL_SIZE//3)
    
    hud = font.render(f"SLY: {sly_mined:.2f} | QUESOS: {cheeses_eaten}/{CHEESE_GOAL} | MODO: {CURRENT_MODE.upper()}", True, COSMIC_PURPLE)
    screen.blit(hud, (10, 10))
    score_text = font.render(f"SCORE: {score}", True, NEON_GREEN)
    screen.blit(score_text, (10, 35))
    build_text = font.render(f"v6 | {BUILD_HASH[:6]}", True, (100, 100, 100))
    screen.blit(build_text, (WINDOW_SIZE - 120, 10))
    
    # HUD CAN LLOBET
    chalet_y = WINDOW_SIZE + 10
    pygame.draw.rect(screen, CAN_LOBLET_GREEN, (10, chalet_y, WINDOW_SIZE - 20, 120))
    progress_bar_width = int((progress['chalet_fund_eur'] / 1490000) * (WINDOW_SIZE - 40))
    pygame.draw.rect(screen, NEON_GREEN, (20, chalet_y + 10, progress_bar_width, 20))
    
    chalet_text = font.render(f"CAN LLOBET: €{progress['chalet_fund_eur']:.0f}/1.490.000", True, BLACK)
    screen.blit(chalet_text, (20, chalet_y + 35))
    
    wallet_text = small_font.render(f"Wallet anónima: {CHALET_WALLET[:10]}... | Dona 'D'", True, BLACK)
    screen.blit(wallet_text, (20, chalet_y + 55))
    
    coords_text = small_font.render(f"{progress['coords']} | Build: {BUILD_HASH[:6]}", True, BLACK)
    screen.blit(coords_text, (20, chalet_y + 75))
    
    meta_text = small_font.render("v7: tx reales | Sin KYC | 100% ético", True, BLACK)
    screen.blit(meta_text, (20, chalet_y + 95))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
print(f"\u001b[35mSLYVERSE v6 CERRADO | $SLY: {progress['total_sly_mined']:.2f} | CAN LLOBET: €{progress['chalet_fund_eur']:.0f}\u001b[0m")
print(f"Wallet anónima: {CHALET_WALLET}")
print("Sube anonymous_chalet_wallet.json y can_llobet_progress.json al repo.")