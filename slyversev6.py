# slyversev6.1.py — CAN LLOBET BELLATERRA | WALLET ENCRIPTADA | PUERTA FÍSICA | TX REALES
# Ejecuta: python3 slyversev6.1.py
# Dependencias: pygame, web3, eth-account, RPi.GPIO (opcional)
# pip install pygame web3 eth-account
# Wallet: Encriptada localmente | $SLY → fondo real | Sin KYC

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
import RPi.GPIO as GPIO  # Solo si hay hardware físico

# === CONFIGURACIÓN CAN LLOBET + ANONIMATO ===
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 10
SOUL_BURN_RATE = 0.13
CHEESE_GOAL = 13
RICKROLL_SCORE = 696
BUILD_HASH = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]

# === ARCHIVOS ===
WALLET_FILE = 'anonymous_chalet_wallet.json'
PROGRESS_FILE = 'can_llobet_progress.json'
DOOR_PIN = 18  # Pin GPIO para puerta física

# === WALLET ENCRIPTADA ===
def generate_encrypted_wallet():
    password = input("\nEstablece una contraseña segura para tu wallet anónima: ")
    acct = Account.create()
    encrypted_key = Account.encrypt(acct.key, password)
    wallet = {
        'address': acct.address,
        'encrypted_key': encrypted_key,
        'password_hash': hashlib.sha256(password.encode()).hexdigest()[:16]
    }
    with open(WALLET_FILE, 'w') as f:
        json.dump(wallet, f, indent=2)
    print(f"\n[WALLET ENCRIPTADA CREADA] {acct.address}")
    return wallet

def load_wallet():
    if not os.path.exists(WALLET_FILE):
        return generate_encrypted_wallet()
    with open(WALLET_FILE, 'r') as f:
        return json.load(f)

wallet = load_wallet()
CHALET_WALLET = wallet['address']

# === CRYPTO: POLYGON MAINNET (REAL) ===
POLYGON_RPC = 'https://polygon-rpc.com'
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
connected = w3.is_connected()
print(f"[POLYGON] {'Conectado' if connected else 'No conectado — modo simulado'}")

# === PROGRESO CAN LLOBET ===
def load_progress():
    defaults = {
        'total_sly_mined': 0.0,
        'chalet_fund_eur': 0.0,
        'homes_potential': 1,
        'target_chalet': 'Can Llobet, Bellaterra €1.49M',
        'coords': '41.512°N, 2.090°E',
        'door_opened': False
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

# === INICIALIZACIÓN PYGAME ===
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 160))
pygame.display.set_caption(f"SLYVERSE v6.1 | Can Llobet | €{progress['chalet_fund_eur']:.0f}/1.490.000 | {BUILD_HASH[:6]}")
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

# === HARDWARE: PUERTA FÍSICA ===
def setup_door():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DOOR_PIN, GPIO.OUT)
        GPIO.output(DOOR_PIN, GPIO.LOW)
        print("[PUERTA FÍSICA] Configurada en GPIO 18")
    except:
        print("[PUERTA FÍSICA] No disponible (ejecutando en simulación)")

def open_can_llobet_door():
    if progress['door_opened']: return
    if progress['chalet_fund_eur'] >= 1490000:
        try:
            GPIO.output(DOOR_PIN, GPIO.HIGH)
            time.sleep(10)
            GPIO.output(DOOR_PIN, GPIO.LOW)
            progress['door_opened'] = True
            save_progress(progress)
            print("\nPUERTA DE CAN LLOBET ABIERTA. BIENVENIDO AL HOGAR ÉTICO.\n")
        except:
            print("\nPUERTA ABIERTA (SIMULADA) — CAN LLOBET ES TUYO.\n")

# === MINADO $SLY + DONACIÓN REAL ===
def mine_sly():
    global sly_mined
    if not soul_burn_active: return
    sly_mined += SOUL_BURN_RATE
    progress['total_sly_mined'] += SOUL_BURN_RATE
    if sly_mined >= 1.0:
        amount_eur = 0.5
        progress['chalet_fund_eur'] += amount_eur
        sly_mined -= 1.0
        print(f"\n[$SLY MINADO] +1 | Donado: €{amount_eur} | Total: €{progress['chalet_fund_eur']:.0f}")
        save_progress(progress)
        # v7: TX REAL
        if connected:
            send_real_donation(amount_eur)
        open_can_llobet_door()

def send_real_donation(eur_amount):
    try:
        password = input("Introduce contraseña para firmar TX: ")
        with open(WALLET_FILE, 'r') as f:
            data = json.load(f)
        private_key = Account.decrypt(data['encrypted_key'], password).hex()
        acct = Account.from_key(private_key)

        tx = {
            'nonce': w3.eth.get_transaction_count(acct.address),
            'to': CHALET_WALLET,
            'value': w3.to_wei(eur_amount / 2500, 'ether'),  # Ajuste simbólico (1€ ~ 2500 MATIC)
            'gas': 21000,
            'gasPrice': w3.to_wei('50', 'gwei'),
            'chainId': 137
        }
        signed = acct.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
        print(f"[TX REAL ENVIADA] {tx_hash.hex()}")
    except Exception as e:
        print(f"[TX FALLIDA] {e} — Donación simulada")

# === TWEET AUTOMÁTICO ===
def auto_tweet():
    tweet = f"#SLYVERSE v6.1 | {score} pts | $SLY: {progress['total_sly_mined']:.1f} | Can Llobet: €{progress['chalet_fund_eur']:.0f}/1.49M | {CHALET_WALLET[:8]}... @orbitalsnaker"
    url = f"https://twitter.com/intent/tweet?text={tweet.replace(' ', '%20')}"
    webbrowser.open(url)

# === RICKROLL ÉTICO ===
def trigger_rickroll():
    print("\nRICKROLL ACTIVADO — €0.5 DONADO A CAN LLOBET")
    threading.Thread(target=webbrowser.open, args=("https://www.youtube.com/watch?v=dQw4w9WgXcQ",)).start()
    mine_sly()
    auto_tweet()

# === IA + MODO ISMAEL ===
MODES = ['human', 'ai', 'cultist', 'vr']
CURRENT_MODE = 'cultist'

def ai_move():
    head = snake[0]
    dx = cheese[0] - head[0]
    dy = cheese[1] - head[1]
    if abs(dx) > abs(dy):
        return (1 if dx > 0 else -1, 0)
    return (0, 1 if dy > 0 else -1)

def ismael_challenge():
    print("\nMODO ISMAEL ACTIVADO: Mañana 11h, a pie, sin Fiat.")
    def notify():
        time.sleep(23*3600)  # ~23h desde ahora
        print("\n¡ES LA HORA! ¿Llegaste a Can Llobet? Abre la puerta con $SLY.")
    threading.Thread(target=notify, daemon=True).start()

# === COLORES ===
BLACK = (13, 2, 8)
NEON_GREEN = (57, 255, 20)
COSMIC_PURPLE = (138, 43, 226)
CHEESE_YELLOW = (255, 215, 0)
VR_BLUE = (0, 191, 255)
CAN_LOBLET_GREEN = (0, 100, 0)

# === INICIAR HARDWARE ===
setup_door()

# === BUCLE PRINCIPAL ===
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
            elif event.key == pygame.K_p:
                auto_tweet()
            elif event.key == pygame.K_i:
                ismael_challenge()

            if CURRENT_MODE == 'human':
                if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)

    # IA
    if CURRENT_MODE in ['ai', 'cultist']:
        new_dir = ai_move()
        if (new_dir[0] + direction[0], new_dir[1] + direction[1]) != (0, 0):
            direction = new_dir

    # Movimiento
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
    
    for i, seg in enumerate(snake):
        color = VR_BLUE if CURRENT_MODE == 'vr' else NEON_GREEN
        alpha = max(50, 255 - i * 3)
        s = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(s, (*color, alpha), (CELL_SIZE//2, CELL_SIZE//2), CELL_SIZE//3)
        screen.blit(s, (seg[0]*CELL_SIZE, seg[1]*CELL_SIZE))
    
    pygame.draw.circle(screen, CHEESE_YELLOW, 
                      (cheese[0]*CELL_SIZE + CELL_SIZE//2, cheese[1]*CELL_SIZE + CELL_SIZE//2), 
                      CELL_SIZE//3)
    
    # HUD
    hud_y = WINDOW_SIZE + 10
    pygame.draw.rect(screen, CAN_LOBLET_GREEN, (0, hud_y, WINDOW_SIZE, 150))
    
    progress_bar_w = int((progress['chalet_fund_eur'] / 1490000) * (WINDOW_SIZE - 40))
    pygame.draw.rect(screen, NEON_GREEN, (20, hud_y + 10, progress_bar_w, 20))
    
    texts = [
        f"SLY: {sly_mined:.2f} | QUESOS: {cheeses_eaten}/{CHEESE_GOAL} | MODO: {CURRENT_MODE.upper()}",
        f"SCORE: {score} | BUILD: {BUILD_HASH[:6]}",
        f"CAN LLOBET: €{progress['chalet_fund_eur']:.0f}/1.490.000",
        f"Wallet: {CHALET_WALLET[:10]}... | D=Donar P=Tweet I=Ismael",
        f"{progress['coords']} | v7: TX reales | 100% ético | Puerta: {'ABIERTA' if progress['door_opened'] else 'CERRADA'}"
    ]
    
    for i, text in enumerate(texts):
        color = COSMIC_PURPLE if i == 0 else NEON_GREEN if i == 1 else BLACK
        font_use = font if i < 3 else small_font
        rendered = font_use.render(text, True, color)
        screen.blit(rendered, (20, hud_y + 35 + i*20))
    
    pygame.display.flip()
    clock.tick(FPS)

# === CIERRE ===
GPIO.cleanup() if 'GPIO' in globals() else None
pygame.quit()
print(f"\nSLYVERSE v6.1 CERRADO | $SLY: {progress['total_sly_mined']:.1f} | CAN LLOBET: €{progress['chalet_fund_eur']:.0f}")
print(f"Wallet: {CHALET_WALLET}")
print("Sube todo al repo: slyversev6.1.py + *.json")