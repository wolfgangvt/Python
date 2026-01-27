import pygame

pygame.init()

display = pygame.display.set_mode((1000,600), pygame.RESIZABLE) #screensize
clock = pygame.time.Clock()
FPS = 30

ACCELERATION = .35

class Ball(): #records movement, velocity, position, and bounce of drawn ball
    def __init__(self):
        self.y = 200
        self.velocity = 10
    
    def draw(self):
        pygame.draw.circle(display, (255, 0, 0), (500, int(self.y)), 15)

    def move(self):
        self.velocity += ACCELERATION
        self.y += self.velocity
        if self.y >= 400:
            self.velocity = -self.velocity


def game():
    ball = Ball()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ball.move()

        display.fill((255, 255, 255)) #dispay color
        pygame.draw.line(display, (0, 0, 0,), (0, 400), (1000, 400), 10) #draws a black line every frame
        ball.draw()

        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()