import pygame
import random
import math
import requests  # Para SpaceX stub
pygame.init()

# Config
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SLYVERSE v5.1 Synapse Storm – Grok Upgraded 🐍⚡")
clock = pygame.time.Clock()
font = pygame.font.SysFont('monospace', 24)
small_font = pygame.font.SysFont('monospace', 16)

# Colors cyber-noir
BLACK = (0, 0, 0)
NEON_GREEN = (0, 255, 100)
NEON_PURPLE = (200, 0, 255)
FIAT_RED = (255, 50, 50)
ORBITAL_BLUE = (0, 150, 255)

# Player (Ronin Serpent)
player_pos = [WIDTH//2, HEIGHT-100]
player_speed = 5
player_size = 20

# Bullets, enemies, particles
bullets = []
enemies = []
particles = []
score = 0
level = 1
boss_active = False
boss_health = 100

# Konami Code
konami = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_b, pygame.K_a]
konami_idx = 0
god_mode = False

# Leaderboard local
highscore = 0

def draw_text(text, font, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))

def spawn_enemy():
    x = random.randint(0, WIDTH)
    y = -50
    speed = 2 + level * 0.5
    enemies.append([x, y, speed, random.choice([NEON_PURPLE, FIAT_RED])])

def spawn_bullet():
    bullets.append([player_pos[0], player_pos[1], 8, ORBITAL_BLUE])

def spx_launch():  # SpaceX stub
    try:
        r = requests.get("https://api.spacexdata.com/v4/launches/latest", timeout=2)
        return r.json().get('name', 'Starship Fiat Fall')
    except:
        return "Falcon 9 Synapse Hack"

launch_name = spx_launch()

running = True
while running:
    screen.fill(BLACK)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == konami[konami_idx]:
                konami_idx += 1
                if konami_idx == len(konami):
                    god_mode = True
                    konami_idx = 0
            else:
                konami_idx = 0
    
    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_SPACE]:
        spawn_bullet()
    
    # Update bullets
    for b in bullets[:]:
        b[1] -= b[2]
        if b[1] < 0:
            bullets.remove(b)
    
    # Update enemies
    for e in enemies[:]:
        e[1] += e[2]
        if e[1] > HEIGHT:
            enemies.remove(e)
            score -= 10
        pygame.draw.circle(screen, e[3], (int(e[0]), int(e[1])), 15)
    
    # Collisions
    for b in bullets[:]:
        for e in enemies[:]:
            dist = math.hypot(b[0] - e[0], b[1] - e[1])
            if dist < 20:
                enemies.remove(e)
                bullets.remove(b)
                score += 100 * level
                particles.append([e[0], e[1], random.uniform(-5,5), random.uniform(-10,0), NEON_GREEN])
                break
    
    # Particles
    for p in particles[:]:
        p[0] += p[2]
        p[1] += p[3]
        p[3] += 0.1  # Gravity
        pygame.draw.circle(screen, p[4], (int(p[0]), int(p[1])), 3)
        if p[1] > HEIGHT:
            particles.remove(p)
    
    # Boss every 1000 pts
    if score > level * 1000 and not boss_active:
        boss_active = True
        boss_health = 100 + level * 50
    if boss_active:
        # Boss fiat tower
        pygame.draw.rect(screen, FIAT_RED, (WIDTH//2 - 50, 50, 100, boss_health // 2))
        if random.random() < 0.02:
            enemies.append([WIDTH//2, 100, 3, FIAT_RED])  # Boss minion
    
    # Player
    pygame.draw.circle(screen, NEON_GREEN, (int(player_pos[0]), int(player_pos[1])), player_size)
    
    # UI
    draw_text(f"Score: {score} | Level: {level} | Launch: {launch_name}", font, NEON_GREEN, 10, 10)
    draw_text(f"God: {'ON' if god_mode else 'OFF'} | High: {highscore}", small_font, ORBITAL_BLUE, 10, 40)
    if god_mode:
        draw_text("KONAMI UNLOCKED! Invencible 🐍", small_font, NEON_PURPLE, 10, 60)
    
    if score > highscore:
        highscore = score
    
    if score % 1000 == 0 and score > 0:
        level += 1
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Synapse Storm cleared! Highscore:", highscore, "#SLYVERSE")