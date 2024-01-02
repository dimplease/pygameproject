import pygame
from main import Fighter



pygame.init()
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level2')

clock = pygame.time.Clock()

background = pygame.image.load('background.jpg').convert_alpha()

def drawing_background():
    scaled_background = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(scaled_background, (0, 0))

firstfighter = Fighter(200, 310)
secondfighter = Fighter(700, 310)




action = True
while action:
    clock.tick(60)
    drawing_background()
    firstfighter.moving()
    #secondfighter.moving()
    firstfighter.draw(screen)
    secondfighter.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = False

    pygame.display.update()
pygame.quit()