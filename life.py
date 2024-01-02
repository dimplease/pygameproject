import pygame
from main9 import Fighter
from main10 import Fighter1

pygame.init()

#создание окна игры
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Shadow Fight')

#установить частоту кадров
clock = pygame.time.Clock()
FPS = 60

#определяет цвета
pink = (241, 156, 187)
white = (255, 255, 255)
red = (255, 0, 0)

#определите переменные истребителя
warrior1_size = 108
warrior1_hight = 130
warrior1_scale = 2
warrior1_offset = [29]
warrior1_data = [warrior1_size, warrior1_hight, warrior1_scale, warrior1_offset]

warrior2_size = 81
warrior2_hight = 108
warrior2_scale = 2
warrior2_offset = [11]
warrior2_data = [warrior2_size, warrior2_hight, warrior2_scale, warrior2_offset]

#загрузка фона игры
fr_image = pygame.image.load('Природа пиксель арт.jpg').convert_alpha()

#загружать таблицы спрайтов
warrior1 = pygame.image.load('Okura.png').convert_alpha()
warrior2 = pygame.image.load('Manx.png').convert_alpha()


#определение количества шагов в анимации
warrior1_steps = [4, 4, 4, 3, 6, 3]
warrior2_steps = [3, 3, 4, 8, 4, 4]


#функция рисования фона
def draw_fr():
    scaled_fr = pygame.transform.scale(fr_image, (screen_width, screen_height))
    screen.blit(scaled_fr, (0, 0))


#функция рисования полосок здоровья бойца
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, white, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, red, (x, y, 400, 30))
    pygame.draw.rect(screen, pink, (x, y, ratio * 400, 30))


#создание двух экземпляров бойцов
fighter_1 = Fighter(200, 350, warrior1_data, warrior1, warrior1_steps)
fighter_2 = Fighter1(700, 350, warrior2_data, warrior2, warrior2_steps)

#игровой цикл
running = True
while running:

    clock.tick(FPS)

    #рисунок фона
    draw_fr()

    #показать здоровье игрока
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)


    #перемещение бойцов
    fighter_1.move(screen_width, screen_height, screen, fighter_2)
    fighter_2.move(screen_width, screen_height, screen, fighter_1)

    #обновление бойцов
    fighter_1.update()
    fighter_2.update()

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
