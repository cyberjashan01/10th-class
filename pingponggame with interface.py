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
TOP_BOTTOM_PADDLE_WIDTH = 100  # Width of top and bottom paddles
TOP_BOTTOM_PADDLE_HEIGHT = 10
FONT_SIZE = 36

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("4-Player Ping Pong Game")

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

        # Ball collision with top and bottom walls
        if self.y - BALL_RADIUS <= 0 or self.y + BALL_RADIUS >= SCREEN_HEIGHT:
            self.speed_y *= -1

        # Ball collision with side paddles
        if self.x - BALL_RADIUS <= PADDLE_WIDTH and left_paddle.rect.top < self.y < left_paddle.rect.bottom:
            self.speed_x *= -1
        if self.x + BALL_RADIUS >= SCREEN_WIDTH - PADDLE_WIDTH and right_paddle.rect.top < self.y < right_paddle.rect.bottom:
            self.speed_x *= -1

        # Ball collision with top and bottom paddles
        if self.y - BALL_RADIUS <= TOP_BOTTOM_PADDLE_HEIGHT and top_paddle.rect.left < self.x < top_paddle.rect.right:
            self.speed_y *= -1
        if self.y + BALL_RADIUS >= SCREEN_HEIGHT - TOP_BOTTOM_PADDLE_HEIGHT and bottom_paddle.rect.left < self.x < bottom_paddle.rect.right:
            self.speed_y *= -1

        # Ball out of bounds for left and right paddles
        if self.x < 0:
            right_paddle.score += 1
            self.reset()
        if self.x > SCREEN_WIDTH:
            left_paddle.score += 1
            self.reset()

        # Ball out of bounds for top and bottom paddles
        if self.y < 0:
            bottom_paddle.score += 1
            self.reset()
        if self.y > SCREEN_HEIGHT:
            top_paddle.score += 1
            self.reset()

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x *= -1  # Change direction
        self.speed_y *= -1

# Paddle class
class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed_x = 0
        self.speed_y = 0
        self.score = 0

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        # Prevent the side paddles from moving out of bounds
        if self.rect.left == 10 or self.rect.right == SCREEN_WIDTH - 10:
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

        # Prevent the top and bottom paddles from moving out of bounds
        if self.rect.top == 10 or self.rect.bottom == SCREEN_HEIGHT - 10:
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.right >= SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

# Create game objects
ball = Ball()
left_paddle = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = Paddle(SCREEN_WIDTH - PADDLE_WIDTH - 10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
top_paddle = Paddle(SCREEN_WIDTH // 2 - TOP_BOTTOM_PADDLE_WIDTH // 2, 10, TOP_BOTTOM_PADDLE_WIDTH, TOP_BOTTOM_PADDLE_HEIGHT)
bottom_paddle = Paddle(SCREEN_WIDTH // 2 - TOP_BOTTOM_PADDLE_WIDTH // 2, SCREEN_HEIGHT - TOP_BOTTOM_PADDLE_HEIGHT - 10, TOP_BOTTOM_PADDLE_WIDTH, TOP_BOTTOM_PADDLE_HEIGHT)

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
            # Left paddle (Player 1)
            if event.key == pygame.K_w:
                left_paddle.speed_y = -PADDLE_SPEED
            if event.key == pygame.K_s:
                left_paddle.speed_y = PADDLE_SPEED
            # Right paddle (Player 2)
            if event.key == pygame.K_UP:
                right_paddle.speed_y = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                right_paddle.speed_y = PADDLE_SPEED
            # Top paddle (Player 3)
            if event.key == pygame.K_a:
                top_paddle.speed_x = -PADDLE_SPEED
            if event.key == pygame.K_d:
                top_paddle.speed_x = PADDLE_SPEED
            # Bottom paddle (Player 4)
            if event.key == pygame.K_LEFT:
                bottom_paddle.speed_x = -PADDLE_SPEED
            if event.key == pygame.K_RIGHT:
                bottom_paddle.speed_x = PADDLE_SPEED
            # Reset the game when 'R' is pressed
            if event.key == pygame.K_r:
                left_paddle.score = 0
                right_paddle.score = 0
                top_paddle.score = 0
                bottom_paddle.score = 0
                ball.reset()

        if event.type == pygame.KEYUP:
            # Stop paddles when keys are released
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle.speed_y = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle.speed_y = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                top_paddle.speed_x = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                bottom_paddle.speed_x = 0

    # Move game objects
    ball.move()
    left_paddle.move()
    right_paddle.move()
    top_paddle.move()
    bottom_paddle.move()

    # Draw game objects
    ball.draw()
    left_paddle.draw()
    right_paddle.draw()
    top_paddle.draw()
    bottom_paddle.draw()

    # Display scores
    left_score_text = font.render(str(left_paddle.score), True, WHITE)
    right_score_text = font.render(str(right_paddle.score), True, WHITE)
    top_score_text = font.render(str(top_paddle.score), True, WHITE)
    bottom_score_text = font.render(str(bottom_paddle.score), True, WHITE)

    screen.blit(left_score_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(right_score_text, (SCREEN_WIDTH * 3 // 4, 20))
    screen.blit(top_score_text, (SCREEN_WIDTH // 2 - 20, 50))
    screen.blit(bottom_score_text, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT - 50))

    # Refresh the screen
    pygame.display.flip()
    clock.tick(60)
