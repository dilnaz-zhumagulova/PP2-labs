import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400  # Screen size
CELL_SIZE = 20  # Size of each snake segment
FPS = 5 # Base speed (increases with levels)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake settings
snake = [(100, 100), (90, 100), (80, 100)]  # Initial position
direction = "RIGHT"

# Generate food function (avoids walls & snake body)
def generate_food():
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:  # Ensure food doesn't spawn on the snake
            return x, y

food = generate_food()

# Score and level system
score = 0
level = 1

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)  # Clear the screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move the snake
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= CELL_SIZE
    elif direction == "DOWN":
        head_y += CELL_SIZE
    elif direction == "LEFT":
        head_x -= CELL_SIZE
    elif direction == "RIGHT":
        head_x += CELL_SIZE

    # Check for wall collision (game over if out of bounds)
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over! Snake hit the wall.")
        running = False

    # Check for self-collision
    if (head_x, head_y) in snake:
        print("Game Over! Snake hit itself.")
        running = False

    # Move snake (add new head, remove tail)
    snake.insert(0, (head_x, head_y))
    
    # Check if food is eaten
    if (head_x, head_y) == food:
        score += 1
        food = generate_food()  # Generate new food position
        # Increase level every 3 points
        if score % 3 == 0:
            level += 1
            FPS += 2  # Increase speed
    else:
        snake.pop()  # Remove last part if no food eaten

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Draw score and level
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)  # Control speed

pygame.quit()