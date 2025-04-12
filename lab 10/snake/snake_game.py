import pygame
import random
import psycopg2
from config import load_config

# Initialize pygame
pygame.init()

# Load DB config and connect
config = load_config(filename=r"C:\Users\zhuma\OneDrive\Рабочий стол\PP2 labs\lab 10\snake\snake_database.ini")  
conn = psycopg2.connect(**config)
cur = conn.cursor()

# Ask username
username = input("Enter your username: ")
cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if not user:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    level = 1
    print("New user created!")
else:
    user_id = user[0]
    cur.execute("SELECT MAX(level) FROM user_score WHERE user_id = %s", (user_id,))
    res = cur.fetchone()
    level = res[0] if res[0] else 1
    print(f"Welcome back, {username}! Current level: {level}")

# Game settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 5 + level - 1

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake settings
snake = [(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"

# Generate food with random weight and size
def generate_food():
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        weight = random.choice([1, 2, 3])  # 1-point, 2-points, 3-points
        size = weight * 10  # 10x10 for 1 point, 20x20 for 3 points
        if (x, y) not in snake:
            return {'pos': (x, y), 'weight': weight, 'size': size, 'timer': pygame.time.get_ticks()}

food = generate_food()
score = 0
level = 1
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    
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
            elif event.key == pygame.K_p:
                cur.execute(
                    "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                    (user_id, score, level)
                )
                conn.commit()
                print("Game paused and saved. Press any key to continue...")
                paused = True
                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.KEYDOWN:
                            paused = False
    
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
    
    # Check for collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or (head_x, head_y) in snake:
        print("Game Over!")
        running = False
    
    # Move snake
    snake.insert(0, (head_x, head_y))
    
    # Check if food is eaten
    if (head_x, head_y) == food['pos']:
        score += food['weight']
        food = generate_food()
        if score % 5 == 0:
            level += 1
            FPS += 1
    else:
        snake.pop()
    
    # Remove food if time exceeded
    if pygame.time.get_ticks() - food['timer'] > 5000:
        food = generate_food()
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    # Draw food with correct size
    pygame.draw.rect(screen, RED, (food['pos'][0], food['pos'][1], food['size'], food['size']))
    
    # Draw score and level
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
