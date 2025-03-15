import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Moving Red Ball')
clock = pygame.time.Clock()

radius = 25
x, y = width // 2, height // 2
speed = 20

running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x - radius - speed >= 0: 
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius + speed <= width: 
        x += speed
    if keys[pygame.K_UP] and y - radius - speed >= 0: 
        y -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= height: 
        y += speed
        
    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, 'red', (x, y), radius)  # Рисуем шар

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()