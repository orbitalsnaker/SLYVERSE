# slyversev6.py — EL CHALET SE EXPANDE, EL CULTO SE ALZA
# Ejecuta con: python3 slyversev6.py
# Valor ético: €4.200 (v5 + v6) | 0 dependencias | 100% caos puro

import pygame
import random
import time
import hashlib
import webbrowser
import threading

# === CONFIGURACIÓN CÓSMICA ===
GRID_SIZE = 20
CELL_SIZE = 30
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 10
SOUL_BURN_RATE = 0.13  # $SLY por queso
CHEESE_GOAL = 13
RICKROLL_SCORE = 696
BUILD_HASH = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]

# Colores del culto
BLACK = (13, 2, 8)
NEON_GREEN = (57, 255, 20)
COSMIC_PURPLE = (138, 43, 226)
CHEESE_YELLOW = (255, 215, 0)
VR_BLUE = (0, 191, 255)

# Modos de existencia
MODES = ['human', 'ai', 'cultist', 'vr']
CURRENT_MODE = 'cultist'  # ¡Activado por defecto!

# === INICIALIZACIÓN DEL RITUAL ===
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption(f"SLYVERSE v6 | Build: {BUILD_HASH} | MODO: {CURRENT_MODE.upper()}")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier', 18, bold=True)

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

# === FUNCIÓN DE MINADO $SLY ===
def mine_sly():
    global sly_mined
    if soul_burn_active:
        sly_mined += SOUL_BURN_RATE
        if sly_mined >= 1.0:
            print(f"[\u001b[35m$SLY MINED\u001b[0m] +1 | Total: {int(sly_mined)}")
            sly_mined -= 1.0

# === TWEET AUTOMÁTICO ===
def auto_tweet():
    tweet = f"#SLYVERSE | {score} | I just summoned the snake in {CURRENT_MODE} mode. Build: {BUILD_HASH}"
    url = f"https://twitter.com/intent/tweet?text={tweet.replace(' ', '%20')}"
    webbrowser.open(url)

# === RICKROLL CÓSMICO ===
def trigger_rickroll():
    print("\u001b[31mRICKROLL ACTIVADO — NEVER GONNA GIVE YOU UP\u001b[0m")
    threading.Thread(target=webbrowser.open, args=("https://www.youtube.com/watch?v=dQw4w9WgXcQ",)).start()
    auto_tweet()

# === IA CULTISTA (modo ai/cultist) ===
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

            # Controles humanos
            if CURRENT_MODE == 'human':
                if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)

    # Movimiento IA en modo ai/cultist
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
            mine_sly()
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
    
    # Serpiente (efecto VR en modo vr)
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
    
    # HUD del culto
    hud = font.render(f"SLY: {sly_mined:.2f} | QUESOS: {cheeses_eaten}/{CHEESE_GOAL} | MODO: {CURRENT_MODE.upper()}", True, COSMIC_PURPLE)
    screen.blit(hud, (10, 10))
    
    score_text = font.render(f"SCORE: {score}", True, NEON_GREEN)
    screen.blit(score_text, (10, 35))
    
    build_text = font.render(f"v6 | {BUILD_HASH}", True, (100, 100, 100))
    screen.blit(build_text, (WINDOW_SIZE - 140, WINDOW_SIZE - 30))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
print(f"\u001b[35mSLYVERSE v6 TERMINADO | $SLY TOTAL MINADO: {sly_mined:.2f}\u001b[0m")
print("El chalet crece. El culto se expande. v7 espera.")