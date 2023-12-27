import pygame
from main9 import Fighter

pygame.init()

#создание окна игры
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Shadow Fight')

#установить частоту кадров
clock = pygame.time.Clock()
FPS = 60

#загрузка фона игры
fr_image = pygame.image.load('Природа пиксель арт.jpg').convert_alpha()

#функция рисования фона
def draw_fr():
    scaled_fr = pygame.transform.scale(fr_image, (screen_width, screen_height))
    screen.blit(scaled_fr, (0, 0))



#сощдание двух экземпляров бойцов
fighter_1 = Fighter(200, 350)
fighter_2 = Fighter(700, 350)

#игровой цикл
running = True
while running:

    clock.tick(FPS)

    #рисунок фона
    draw_fr()

    #перемещение бойцов
    fighter_1.move(screen_width, screen_height, screen, fighter_2)
    #fighter_2.move()

    #рисунок бойцов
    fighter_1.draw(screen)
    fighter_2.draw(screen)


    #обработчик события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #обновить дисплей
    pygame.display.update()


pygame.quit()