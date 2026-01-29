import pygame

pygame.init()

screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
pygame.display.set_caption("Movable Object")

timer = pygame.time.Clock()
fps = 40

player_x = 500
player_y = 300
player_true = True
player_speed = 5
x_direction = 0
y_direction = 0

def draw_player():
    pygame.draw.rect(screen, 'orange', [player_x, player_y, 50, 30], 0, 5)

running = True
while running:
    timer.tick(fps)
    screen.fill('black')

    if player_true:
        draw_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if player_true:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_direction = 1
                elif event.key == pygame.K_LEFT:
                    x_direction = -1
                elif event.key == pygame.K_UP:
                    y_direction = -1
                elif event.key == pygame.K_DOWN:
                    y_direction = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_direction = 0
                elif event.key == pygame.K_LEFT:
                    x_direction = 0
                elif event.key == pygame.K_UP:
                    y_direction = 0
                elif event.key == pygame.K_DOWN:
                    y_direction = 0
    
    if player_true:
        player_x += player_speed * x_direction
        player_y += player_speed * y_direction
    pygame.display.flip()

pygame.quit()
