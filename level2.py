import pygame
from main import Fighter


pygame.init()
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level2')

clock = pygame.time.Clock()

counter = 3
lastcounter = pygame.time.get_ticks()
score = [0, 0]
gameover = False
gameovercooldown = 2000


codysize = 110
codyscale = 2
codyoffset = [35, -15]
codydata = [codysize, codyscale, codyoffset]
shadowsize = 95
shadowscale = 2
shadowoffset = [20, -3]
shadowdata = [shadowsize, shadowscale, shadowoffset]


background = pygame.image.load('background.jpg').convert_alpha()
cody_sheet = pygame.image.load('codymain.png').convert_alpha()
shadow_sheet = pygame.image.load('shadowmain.png').convert_alpha()
victorypicture = pygame.image.load('victory.png').convert_alpha()

codysteps = [3, 3, 3, 2]
shadowsteps = [3, 3, 2, 3]
def drawing_background():
    scaled_background = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(scaled_background, (0, 0))

countfont = pygame.font.Font('turok.ttf', 80)

def drawtext(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
def xp_bar(xp, x, y):
    ratio = xp / 100
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 400, 30))
    pygame.draw.rect(screen, (255, 255, 0), (x, y, 400 * ratio, 30))


firstfighter = Fighter(1, 200, 310, False, codydata, cody_sheet, codysteps)
secondfighter = Fighter(2, 700, 310, True, shadowdata, shadow_sheet, shadowsteps)




action = True
while action:
    clock.tick(60)
    drawing_background()
    xp_bar(firstfighter.xp, 20, 20)
    xp_bar(secondfighter.xp, 580, 20)
    if counter <= 0:
        firstfighter.moving(screen, secondfighter, gameover)
        secondfighter.moving(screen, firstfighter, gameover)
    else:
        drawtext(str(counter), countfont, (255, 0, 0), 500, 200)
        if (pygame.time.get_ticks() - lastcounter) >= 1000:
            counter -= 1
            lastcounter = pygame.time.get_ticks()

    firstfighter.updating()
    secondfighter.updating()
    firstfighter.draw(screen)
    secondfighter.draw(screen)

    if gameover is False:
        if firstfighter.alive == False:
            score[1] += 1
            gameover = True
            gameovertime = pygame.time.get_ticks()
        elif secondfighter.alive == False:
            score[0] += 1
            gameover = True
            gameovertime = pygame.time.get_ticks()
    else:
        screen.blit(victorypicture, (360, 150))
        if pygame.time.get_ticks() - gameovertime > gameovercooldown:
            gameover = False
            counter = 3
            firstfighter = Fighter(1, 200, 310, False, codydata, cody_sheet, codysteps)
            secondfighter = Fighter(2, 700, 310, True, shadowdata, shadow_sheet, shadowsteps)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action = False

    pygame.display.update()
pygame.quit()
