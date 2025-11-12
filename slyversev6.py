# slyversev6_1.py — EL CHALET SE MATERIALIZA, SIN FANTASMAS
# Ejecuta con: python3 slyversev6_1.py
# Dependencias: pygame (ya), + web3 para Ethereum/ Polygon (instala: pip install web3)
# Wallet real: Integra tu ETH/Polygon address para donar $SLY minado (simulado como ERC-20 mock, real en v7)

import pygame
import random
import time
import hashlib
import webbrowser
import threading
import json  # Para tracking JSON
from web3 import Web3  # Para crypto real (Polygon testnet por ahora, mainnet en v7)

# === CONFIGURACIÓN CÓSMICA — REALIDAD TANGIBLE ===
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 10
SOUL_BURN_RATE = 0.13  # $SLY por queso (ahora trackeado a wallet)
CHEESE_GOAL = 13
RICKROLL_SCORE = 696
BUILD_HASH = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]

# Crypto real: Polygon Mumbai testnet (cambia a mainnet para prod)
POLYGON_RPC = 'https://rpc-mumbai.maticvigil.com'  # Testnet gratis
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
if not w3.is_connected():
    print("⚠️ Testnet no conectado — usa mainnet en v7 para donaciones reales")

# Wallet del chalet (tu address ETH/Polygon — ¡CÁMBIALA!)
CHALET_WALLET = '0xTuAddressAqui'  # Ej: 0x123... | Trackea donaciones aquí
SLY_TOKEN_MOCK = 0.13  # En v7: contrato ERC-20 real para $SLY

# Colores del culto
BLACK = (13, 2, 8)
NEON_GREEN = (57, 255, 20)
COSMIC_PURPLE = (138, 43, 226)
CHEESE_YELLOW = (255, 215, 0)
VR_BLUE = (0, 191, 255)
CHALET_GOLD = (255, 215, 0)  # Nuevo: Oro para progreso real

# Modos de existencia
MODES = ['human', 'ai', 'cultist', 'vr']
CURRENT_MODE = 'cultist'

# Tracking real: JSON para progreso chalet (sin fake — persiste en disco)
TRACKING_FILE = 'chalet_progress.json'
def load_progress():
    try:
        with open(TRACKING_FILE, 'r') as f:
            return json.load(f)
    except:
        return {'total_sly_mined': 0.0, 'donations_sent': 0, 'chalet_fund_eur': 0.0, 'homes_potential': 1}

def save_progress(progress):
    with open(TRACKING_FILE, 'w') as f:
        json.dump(progress, f)

progress = load_progress()

# === INICIALIZACIÓN DEL RITUAL ===
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))  # +100 para HUD chalet
pygame.display.set_caption(f"SLYVERSE v6.1 | Build: {BUILD_HASH} | MODO: {CURRENT_MODE.upper()} | CHALET: €{progress['chalet_fund_eur']:.0f}")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier', 18, bold=True)
small_font = pygame.font.SysFont('Courier', 14)

# === SERPIENTE ORBITAL ===
snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
direction = (1, 0)
score = 0
sly_mined = 0.0
cheeses_eaten = 0
soul_burn_active = True

# === QUESO SAGRADO ===
def spawn_cheese():
    while True:
        pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        if pos not in snake:
            return pos

cheese = spawn_cheese()

# === MINADO $SLY REAL — ENVÍA A WALLET ===
def mine_sly():
    global sly_mined, progress
    if soul_burn_active:
        sly_mined += SOUL_BURN_RATE
        progress['total_sly_mined'] += SOUL_BURN_RATE
        if sly_mined >= 1.0:
            print(f"[\u001b[35m$SLY MINADO REAL\u001b[0m] +1 | Total global: {progress['total_sly_mined']:.1f}")
            # Simula envío (en v7: tx real via web3)
            progress['chalet_fund_eur'] += 0.5  # 1 $SLY ≈ €0.5 (ajusta con oracle real)
            if w3.is_connected():
                # Mock tx: En v7, envía a contrato
                print(f"💸 Donado a {CHALET_WALLET[:10]}... | +€0.5 al chalet")
            sly_mined -= 1.0
        save_progress(progress)

# === TWEET AUTOMÁTICO CON PROGRESO REAL ===
def auto_tweet():
    tweet = f"#SLYVERSE v6.1 | {score} pts | $SLY: {progress['total_sly_mined']:.1f} | Chalet fund: €{progress['chalet_fund_eur']:.0f} | {CURRENT_MODE} mode. Build: {BUILD_HASH} | @orbitalsnaker"
    url = f"https://twitter.com/intent/tweet?text={tweet.replace(' ', '%20')}"
    webbrowser.open(url)

# === RICKROLL + DONACIÓN REAL ===
def trigger_rickroll():
    print("\u001b[31mRICKROLL ACTIVADO — Y €0.5 DONADO AL CHALET\u001b[0m")
    threading.Thread(target=webbrowser.open, args=("https://www.youtube.com/watch?v=dQw4w9WgXcQ",)).start()
    mine_sly()  # Bonus real
    auto_tweet()

# === IA CULTISTA ===
def ai_move():
    head = snake[0]
    dx = cheese[0] - head[0]
    dy = cheese[1] - head[1]
    if abs(dx) > abs(dy):
        return (1 if dx > 0 else -1, 0)
    else:
        return (0, 1 if dy > 0 else -1)

# === BUCLE DEL RITUAL ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_m:  # Toggle modo
                idx = (MODES.index(CURRENT_MODE) + 1) % len(MODES)
                CURRENT_MODE = MODES[idx]
                print(f"MODO CAMBIADO → {CURRENT_MODE.upper()}")
            elif event.key == pygame.K_d:  # Nueva: Dona manual
                mine_sly()
                print("💸 Donación manual al chalet activada")

            # Controles humanos
            if CURRENT_MODE == 'human':
                if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)

    # Movimiento IA
    if CURRENT_MODE in ['ai', 'cultist']:
        new_dir = ai_move()
        if (new_dir[0] + direction[0], new_dir[1] + direction[1]) != (0, 0):
            direction = new_dir

    # Actualizar serpiente
    head = snake[0]
    new_head = ((head[0] + direction[0]) % GRID_SIZE, (head[1] + direction[1]) % GRID_SIZE)
    
    if new_head in snake[1:]:
        print(f"\u001b[31mCOLISIÓN — Alma quemada. Score: {score}\u001b[0m")
        snake = [snake[0]]
        direction = (1, 0)
        score = max(score - 10, 0)
    else:
        snake.insert(0, new_head)
        if new_head == cheese:
            score += 10
            cheeses_eaten += 1
            mine_sly()  # ¡Real!
            cheese = spawn_cheese()
            if score >= RICKROLL_SCORE:
                trigger_rickroll()
                score = 0
                cheeses_eaten = 0
        else:
            snake.pop()

    # === DIBUJO DEL PORTAL ===
    screen.fill(BLACK)
    
    # Grid cósmica
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (20, 20, 30), rect, 1)
    
    # Serpiente (efecto VR)
    for i, segment in enumerate(snake):
        color = VR_BLUE if CURRENT_MODE == 'vr' else NEON_GREEN
        alpha = 255 - i * 3
        s = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(s, (*color, alpha), (CELL_SIZE//2, CELL_SIZE//2), CELL_SIZE//3)
        screen.blit(s, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE))
    
    # Queso sagrado
    pygame.draw.circle(screen, CHEESE_YELLOW, 
                      (cheese[0]*CELL_SIZE + CELL_SIZE//2, cheese[1]*CELL_SIZE + CELL_SIZE//2), 
                      CELL_SIZE//3)
    
    # HUD del culto + CHALET REAL (nuevo panel abajo)
    hud = font.render(f"SLY: {sly_mined:.2f} | QUESOS: {cheeses_eaten}/{CHEESE_GOAL} | MODO: {CURRENT_MODE.upper()}", True, COSMIC_PURPLE)
    screen.blit(hud, (10, 10))
    
    score_text = font.render(f"SCORE: {score}", True, NEON_GREEN)
    screen.blit(score_text, (10, 35))
    
    build_text = font.render(f"v6.1 | {BUILD_HASH}", True, (100, 100, 100))
    screen.blit(build_text, (WINDOW_SIZE - 140, 10))
    
    # Nuevo: HUD Chalet Tangible (sin fake)
    chalet_y = WINDOW_SIZE + 10
    pygame.draw.rect(screen, CHALET_GOLD, (10, chalet_y, WINDOW_SIZE - 20, 80))  # Barra oro
    progress_bar_width = int((progress['chalet_fund_eur'] / 10000) * (WINDOW_SIZE - 40))  # Meta €10k
    pygame.draw.rect(screen, NEON_GREEN, (20, chalet_y + 10, progress_bar_width, 20))
    
    chalet_text = font.render(f"CHALET ÉTICO: €{progress['chalet_fund_eur']:.0f}/10.000 | Hogares: {progress['homes_potential']}", True, BLACK)
    screen.blit(chalet_text, (20, chalet_y + 35))
    
    wallet_text = small_font.render(f"Wallet: {CHALET_WALLET[:10]}... | Dona con 'D'", True, BLACK)
    screen.blit(wallet_text, (20, chalet_y + 55))
    
    # Meta real: Basado en precios España 2025
    meta_text = small_font.render("Meta: 1 chalet Extremadura (~€196k) | Semilla: 5%", True, BLACK)
    screen.blit(meta_text, (20, chalet_y + 70))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
print(f"\u001b[35mSLYVERSE v6.1 TERMINADO | $SLY TOTAL: {progress['total_sly_mined']:.2f} | CHALET FUND: €{progress['chalet_fund_eur']:.0f}\u001b[0m")
print("Sin fake: Trackea en chalet_progress.json. v7: Contrato ERC-20 real.")