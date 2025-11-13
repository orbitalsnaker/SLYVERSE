import pygame
import random
import math
pygame.init()

# Config
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SLYVERSE v8.1 Apocalipsis Coil – Grok Apocalipsis 🐍☄️")
clock = pygame.time.Clock()
font = pygame.font.SysFont('monospace', 28)
small_font = pygame.font.SysFont('monospace', 18)

# Colors
BLACK = (0,0,0)
COIL_GOLD = (255, 215, 0)
APOCALYPSE_ORANGE = (255, 140, 0)
FIAT_GRAY = (128, 128, 128)
NEON_SNAKE = (0, 255, 255)

# Serpiente Coil (player1)
coil = [[WIDTH//2, HEIGHT//2]]
coil_dir = (0, -1)
coil_length = 10
speed = 3

# Player2 co-op
p2_pos = [WIDTH//2 + 100, HEIGHT//2]
p2_size = 15
p2_speed = 4

# Enemies fiat, powerups
fiat_towers = []
powerups = []
wave = 1
score = 0
co_op_active = True

# Konami para infinite coil
konami = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_b, pygame.K_a]
konami_idx = 0
infinite = False

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Input P1 (arrows)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: coil_dir = (-1, 0)
    if keys[pygame.K_RIGHT]: coil_dir = (1, 0)
    if keys[pygame.K_UP]: coil_dir = (0, -1)
    if keys[pygame.K_DOWN]: coil_dir = (0, 1)
    
    # Konami
    if event.type == pygame.KEYDOWN and event.key == konami[konami_idx]:
        konami_idx += 1
        if konami_idx == len(konami):
            infinite = True
            konami_idx = 0
    
    # P2 co-op (WASD)
    if co_op_active:
        if keys[pygame.K_a] and p2_pos[0] > 0: p2_pos[0] -= p2_speed
        if keys[pygame.K_d] and p2_pos[0] < WIDTH: p2_pos[0] += p2_speed
        if keys[pygame.K_w] and p2_pos[1] > 0: p2_pos[1] -= p2_speed
        if keys[pygame.K_s] and p2_pos[1] < HEIGHT: p2_pos[1] += p2_speed
        pygame.draw.circle(screen, COIL_GOLD, (int(p2_pos[0]), int(p2_pos[1])), p2_size)
    
    # Update coil
    head = [coil[0][0] + coil_dir[0] * speed, coil[0][1] + coil_dir[1] * speed]
    coil.insert(0, head)
    if len(coil) > coil_length and not infinite:
        coil.pop()
    
    # Spawn fiat towers
    if random.random() < 0.01 + wave * 0.005:
        fiat_towers.append([random.randint(0, WIDTH), 0, 40])  # x,y,size
    
    # Update towers
    for tower in fiat_towers[:]:
        tower[1] += 2 + wave * 0.3
        if tower[1] > HEIGHT:
            fiat_towers.remove(tower)
            score -= 50
        pygame.draw.rect(screen, FIAT_GRAY, (tower[0]-tower[2]//2, tower[1], tower[2], tower[2]))
    
    # Collisions coil vs towers
    for tower in fiat_towers[:]:
        for seg in coil:
            dist = math.hypot(seg[0] - tower[0], seg[1] - tower[1])
            if dist < tower[2]:
                fiat_towers.remove(tower)
                score += 200 * wave
                coil_length += 1
                break
    
    # P2 collisions
    for tower in fiat_towers[:]:
        dist = math.hypot(p2_pos[0] - tower[0], p2_pos[1] - tower[1])
        if dist < tower[2] + p2_size:
            fiat_towers.remove(tower)
            score += 150
    
    # Waves
    if score > wave * 2000:
        wave += 1
    
    # Draw coil (trail effect)
    for i, seg in enumerate(coil):
        alpha = i / len(coil)
        color = (int(NEON_SNAKE[0] * alpha), int(NEON_SNAKE[1] * alpha), int(NEON_SNAKE[2] * alpha))
        pygame.draw.circle(screen, color, (int(seg[0]), int(seg[1])), max(5, int(15 * alpha)))
    
    # UI
    draw_text(f"Apocalipsis Coil v8.1 | Score: {score} | Wave: {wave} | Length: {len(coil)}", font, COIL_GOLD, 10, 10)
    draw_text(f"Infinite: {'ON' if infinite else 'OFF'} | Co-op: ON", small_font, NEON_SNAKE, 10, 50)
    if infinite:
        draw_text("KONAMI: Apocalipsis Defeated! 🐍∞", small_font, APOCALYPSE_ORANGE, 10, 70)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Coil Apocalipsis survived! Score:", score, "#SLYVERSE v8.1")