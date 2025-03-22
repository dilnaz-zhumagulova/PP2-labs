import pygame

pygame.init()

# Screen settings
fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_figure = 0
active_color = (255, 255, 255)  # White as RGB

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []


def draw_menu(color):
    """Draws the top menu with color options and brush shapes."""
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Brush selection
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)

    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)

    brush_list = [circle_brush, rect_brush]

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

    return brush_list, color_rect, rgb_list


def draw_painting(paints):
    """Draws shapes from the stored paint list."""
    for color, pos, figure in paints:
        if figure == -1:  # Eraser
            pygame.draw.rect(screen, (255, 255, 255), [pos[0] - 20, pos[1] - 20, 40, 40])
        elif figure == 0:  # Circle
            pygame.draw.circle(screen, color, pos, 20, 2)
        elif figure == 1:  # Rectangle
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)


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

            for brush in brushes:
                if brush[0].collidepoint(event.pos):
                    active_figure = brush[1]  # Switch between circle and rectangle

    pygame.display.flip()

pygame.quit()