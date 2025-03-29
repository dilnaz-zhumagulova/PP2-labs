import pygame

pygame.init()

# Screen settings
fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_figure = 0  # Default shape (circle)
active_color = (255, 255, 255)  # Default color (white)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []

def draw_menu(color):
    """Draws the top menu with color options and brush shapes."""
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Shape selection buttons
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)

    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)

    square_brush = [pygame.draw.rect(screen, 'black', [130, 10, 50, 50]), 2]
    pygame.draw.rect(screen, 'white', [136, 16, 37, 37], 2)

    right_triangle_brush = [pygame.draw.rect(screen, 'black', [190, 10, 50, 50]), 3]
    pygame.draw.polygon(screen, 'white', [(195, 55), (195, 15), (235, 55)], 2)

    equilateral_triangle_brush = [pygame.draw.rect(screen, 'black', [250, 10, 50, 50]), 4]
    pygame.draw.polygon(screen, 'white', [(275, 15), (255, 55), (295, 55)], 2)

    rhombus_brush = [pygame.draw.rect(screen, 'black', [310, 10, 50, 50]), 5]
    pygame.draw.polygon(screen, 'white', [(335, 15), (355, 35), (335, 55), (315, 35)], 2)

    brush_list = [circle_brush, rect_brush, square_brush, right_triangle_brush, equilateral_triangle_brush, rhombus_brush]
    
    # Active color indicator
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Eraser button (using a rectangle instead of an image)
    eraser_rect = pygame.draw.rect(screen, (200, 200, 200), [WIDTH - 150, 10, 40, 40])
    pygame.draw.line(screen, 'black', (WIDTH - 140, 15), (WIDTH - 120, 35), 5)
    pygame.draw.line(screen, 'black', (WIDTH - 120, 15), (WIDTH - 140, 35), 5)
    
    # Color palette
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]  # Eraser (white)

    return brush_list,  color_rect, rgb_list


def draw_painting(paints):
    """Draws shapes from the stored paint list."""
    for color, pos, figure in paints:
        x, y = pos
        if figure == -1:  # Eraser
            pygame.draw.rect(screen, (255, 255, 255), [pos[0] - 20, pos[1] - 20, 40, 40])
        elif figure == 0:  # Circle
            pygame.draw.circle(screen, color, pos, 20, 2)
        elif figure == 1:  # Rectangle
            pygame.draw.rect(screen, color, [x - 15, y - 15, 37, 20], 2)
        elif figure == 2:  # Square
            pygame.draw.rect(screen, color, [x - 20, y - 20, 40, 40], 2)
        elif figure == 3:  # Right triangle
            pygame.draw.polygon(screen, color, [(x, y), (x + 30, y), (x, y - 30)], 2)
        elif figure == 4:  # Equilateral triangle
            pygame.draw.polygon(screen, color, [(x, y - 30), (x - 25, y + 15), (x + 25, y + 15)], 2)
        elif figure == 5:  # Rhombus
            pygame.draw.polygon(screen, color, [(x, y - 25), (x + 25, y), (x, y + 25), (x - 25, y)], 2)

# Main loop
run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    brushes, colors, rgbs = draw_menu(active_color)

    # Draw while clicking (only below menu bar)
    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure))

    draw_painting(painting)

    # Cursor preview
    if mouse[1] > 85:
        if active_figure == -1:  # Eraser
            pygame.draw.rect(screen, (200, 200, 200), [mouse[0] - 20, mouse[1] - 20, 40, 40], 2)
        elif active_figure == 0:  # Circle
            pygame.draw.circle(screen, active_color, mouse, 20, 2)
        elif active_figure == 1:  # Rectangle
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)
        elif active_figure == 2:  # Square
            pygame.draw.rect(screen, active_color, [mouse[0] - 20, mouse[1] - 20, 40, 40], 2)
        elif active_figure == 3:  # Right triangle
            pygame.draw.polygon(screen, active_color, [(mouse[0], mouse[1]), (mouse[0] + 30, mouse[1]), (mouse[0], mouse[1] - 30)], 2)
        elif active_figure == 4:  # Equilateral triangle
            pygame.draw.polygon(screen, active_color, [(mouse[0], mouse[1] - 30), (mouse[0] - 25, mouse[1] + 15), (mouse[0] + 25, mouse[1] + 15)], 2)
        elif active_figure == 5:  # Rhombus
            pygame.draw.polygon(screen, active_color, [(mouse[0], mouse[1] - 25), (mouse[0] + 25, mouse[1]), (mouse[0], mouse[1] + 25), (mouse[0] - 25, mouse[1])], 2)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
                    if active_color == (255, 255, 255):  # If eraser is selected
                        active_figure = -1  # Special eraser mode
                        
            for i in range(len(brushes)):
                if brushes[i][0].collidepoint(event.pos):
                    active_figure = brushes[i][1]  # Switch between shapes

    pygame.display.flip()

pygame.quit()
