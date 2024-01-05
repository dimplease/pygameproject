import pygame
from main import Fighter


pygame.init()
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level2')

clock = pygame.time.Clock()

codysize = 110
codyscale = 2
codyoffset = [35, -5]
codydata = [codysize, codyscale, codyoffset]
shadowsize = 95
shadowscale = 2
shadowoffset = [20, -3]
shadowdata = [shadowsize, shadowscale, shadowoffset]


background = pygame.image.load('background.jpg').convert_alpha()
cody_sheet = pygame.image.load('codymain.png').convert_alpha()
shadow_sheet = pygame.image.load('shadowmain.png').convert_alpha()

codysteps = [3, 3, 3, 2]
shadowsteps = [3, 3, 2, 3]
def drawing_background():
    scaled_background = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(scaled_background, (0, 0))


def xp_bar(xp, x, y):
    ratio = xp / 100
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 400, 30))
    pygame.draw.rect(screen, (255, 255, 0), (x, y, 400 * ratio, 30))


firstfighter = Fighter(200, 310, codydata, cody_sheet, codysteps)
secondfighter = Fighter(700, 310, shadowdata, shadow_sheet, shadowsteps)




action = True
while action:
    clock.tick(60)
    drawing_background()
    xp_bar(firstfighter.xp, 20, 20)
    xp_bar(secondfighter.xp, 580, 20)

    firstfighter.moving(screen, secondfighter)
    #secondfighter.moving()
    firstfighter.draw(screen)
    secondfighter.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = False

    pygame.display.update()
pygame.quit()
