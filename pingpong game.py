import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7
FONT_SIZE = 36

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Font for displaying the score
font = pygame.font.Font(None, FONT_SIZE)

# Ball class
class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_RADIUS)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with top and bottom
        if self.y - BALL_RADIUS <= 0 or self.y + BALL_RADIUS >= SCREEN_HEIGHT:
            self.speed_y *= -1

        # Ball collision with paddles
        if self.x - BALL_RADIUS <= PADDLE_WIDTH and left_paddle.rect.top < self.y < left_paddle.rect.bottom:
            self.speed_x *= -1
        if self.x + BALL_RADIUS >= SCREEN_WIDTH - PADDLE_WIDTH and right_paddle.rect.top < self.y < right_paddle.rect.bottom:
            self.speed_x *= -1

        # Ball out of bounds
        if self.x < 0:
            right_paddle.score += 1
            self.reset()
        if self.x > SCREEN_WIDTH:
            left_paddle.score += 1
            self.reset()

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x *= -1  # Change direction

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 0
        self.score = 0

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self):
        self.rect.y += self.speed

        # Prevent the paddle from moving out of bounds
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Create game objects
ball = Ball()
left_paddle = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
right_paddle = Paddle(SCREEN_WIDTH - PADDLE_WIDTH - 10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle.speed = -PADDLE_SPEED
            if event.key == pygame.K_s:
                left_paddle.speed = PADDLE_SPEED
            if event.key == pygame.K_UP:
                right_paddle.speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                right_paddle.speed = PADDLE_SPEED
            if event.key == pygame.K_r:  # Reset the game when 'R' is pressed
                left_paddle.score = 0
                right_paddle.score = 0
                ball.reset()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle.speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle.speed = 0

    # Move game objects
    ball.move()
    left_paddle.move()
    right_paddle.move()

    # Draw game objects
    ball.draw()
    left_paddle.draw()
    right_paddle.draw()

    # Display scores
    left_score_text = font.render(str(left_paddle.score), True, WHITE)
    right_score_text = font.render(str(right_paddle.score), True, WHITE)
    screen.blit(left_score_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(right_score_text, (SCREEN_WIDTH * 3 // 4, 20))

    # Refresh the screen
    pygame.display.flip()
    clock.tick(60)