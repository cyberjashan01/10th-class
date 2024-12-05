import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
player_width = 50
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemies = []
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
game_over_font = pygame.font.SysFont(None, 64)

def move_player(keys, player_x):
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    return player_x

def display_score(score):
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, [10, 10])

def display_game_over():
    game_over_text = game_over_font.render("GAME OVER", True, red)
    screen.blit(game_over_text, [screen_width // 4, screen_height // 2])

def game_loop():
    global score
    player_x = screen_width // 2 - player_width // 2
    player_y = screen_height - player_height - 10
    bullets.clear()
    enemies.clear()
    score = 0

    game_over = False
    running = True

    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullets.append([bullet_x, player_y])

        keys = pygame.key.get_pressed()
        player_x = move_player(keys, player_x)
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)
            else:
                pygame.draw.rect(screen, white, (bullet[0], bullet[1], bullet_width, bullet_height))
        if random.randint(1, 30) == 1 and not game_over:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemies.append([enemy_x, 0])

        for enemy in enemies[:]:
            enemy[1] += enemy_speed
            if enemy[1] > screen_height:
                enemies.remove(enemy)
                game_over = True
            else:
                pygame.draw.rect(screen, red, (enemy[0], enemy[1], enemy_width, enemy_height))

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet[0] > enemy[0] and bullet[0] < enemy[0] + enemy_width and \
                   bullet[1] > enemy[1] and bullet[1] < enemy[1] + enemy_height:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

        pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
        display_score(score)
        if game_over:
            display_game_over()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
game_loop()

"""Description for YouTube:

🎮 Epic Pygame Shooter Game!  🎮

In this video, we're diving into an action-packed Pygame project where we code a classic arcade-style shooter game! Watch as we build this game step-by-step, allowing our player to dodge enemies and shoot them down for points! 
🔹 Features:
- Player Controls: Move left and right to dodge enemies
- Enemy Spawning: Randomized enemies descend from above
- Bullet Shooting: Fire bullets to destroy enemies and score points
- Game Over Screen: Ends the game when an enemy slips past your defenses

💡 What You'll Learn:
- Basic game mechanics with Python and Pygame
- Player movement and collision detection
- Creating and removing bullets and enemies
- Displaying score and Game Over messages

If you're a beginner looking to start game development or a Python programmer ready to have fun with Pygame, this is the perfect project for you! 

Don’t forget to like, subscribe, and hit the notification bell 🔔 for more coding tutorials and game dev content! 

#Pygame #PythonGame #GameDevelopment #PythonProjects #CodingForBeginners #Pygame #PythonGame #GameDevelopment #PythonProjects #CodingForBeginners #IndieGameDev #GameDev #LearnPython #PythonProgramming #CodingTutorial #PythonCoding #ArcadeGame #RetroGaming #CodeWithMe #PythonBeginners #GamingProject #PythonTutorial #TechWithPython #ProgrammingBasics #DevLife #CodeNewbies #PythonLearning
"""
