import pygame
import json

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (192, 192, 192)

# Initialize pygame
pygame.init()

# Set up the screen
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
cell_size = 20
screen_width = m * cell_size
screen_height = n * cell_size + 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grid Simulation")

# Grid state
grid = [[0] * m for _ in range(n)]  # 0: empty, 1: obstacle, 2: start, 3: end
start_point = None
end_point = None

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // cell_size
            col = mouse_pos[0] // cell_size
            if 0 <= row < n and 0 <= col < m:
                if event.button == 1:  # Left click for obstacle
                    grid[row][col] = 1
                elif event.button == 2:  # Middle click for start point
                    if start_point:
                        grid[start_point[0]][start_point[1]] = 0
                    start_point = (row, col)
                    grid[row][col] = 2
                elif event.button == 3:  # Right click for end point
                    if end_point:
                        grid[end_point[0]][end_point[1]] = 0
                    end_point = (row, col)
                    grid[row][col] = 3

    # Draw the grid
    screen.fill(WHITE)
    for i in range(n):
        for j in range(m):
            pygame.draw.rect(screen, GRAY, (j * cell_size, i * cell_size, cell_size, cell_size), 1)
            color = WHITE
            if grid[i][j] == 1:
                color = BLACK
            elif grid[i][j] == 2:
                color = GREEN
            elif grid[i][j] == 3:
                color = RED
            pygame.draw.rect(screen, color, (j * cell_size + 1, i * cell_size + 1, cell_size - 2, cell_size - 2))

    # Draw instructions
    font = pygame.font.Font(None, 24)
    text = font.render("Select Obstacle: Left Click", True, BLACK)
    text_rect = text.get_rect(topleft=(10, n * cell_size + 10))
    screen.blit(text, text_rect)

    text = font.render("Select Start Point: Middle Click", True, BLACK)
    text_rect = text.get_rect(topleft=(10, n * cell_size + 40))
    screen.blit(text, text_rect)

    text = font.render("Select End Point: Right Click", True, BLACK)
    text_rect = text.get_rect(topleft=(10, n * cell_size + 70))
    screen.blit(text, text_rect)

    # Export button
    export_button = pygame.draw.rect(screen, GREEN, (screen_width - 200, n * cell_size + 20, 180, 30))
    text = font.render("Export as JSON", True, WHITE)
    screen.blit(text, (screen_width - 190, n * cell_size + 25))

    # Check if export button clicked
    mouse_pos = pygame.mouse.get_pos()
    if export_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:  # Left click
            data = {
                "n": n,
                "m": m,
                "obstacles": [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1],
                "start": start_point,
                "end": end_point,
                "pop_size": 50,
                "generations": 100
            }
            with open("dumps/grid_config.json", "w") as f:
                json.dump(data, f)

    pygame.display.flip()

# Quit pygame
pygame.quit()
