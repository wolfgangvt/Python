import pygame

pygame.init()

display = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
pygame.display.set_caption("Pygame Clock Example")
clock = pygame.time.Clock()
FPS = 30

font = pygame.font.SysFont("Times New Roman", 20)
text_color = (0, 0, 0)
bg_color = (255, 255, 255)

running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000

    display.fill(bg_color)
    time_surface = font.render(f"Time Elapsed: {elapsed_time} seconds", True, text_color)
    display.blit(time_surface, (10,40))

    pygame.display.flip()

    delta_time = clock.tick(FPS)

pygame.quit()