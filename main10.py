import pygame


class Fighter1:
    def __init__(self, x, y, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.hight = data[1]
        self.image_scale = data[2]
        self.offset = data[3]
        self.flip = True
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0:на месте #1:прыжок #2:атака_1 #3:бег #4:атака_2 #5:смерть
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def load_images(self, sprite, animation_steps):
        #извлечение изображения из таблицы спрайтов
        animation_list = []
        for y, j in enumerate(animation_steps):
            temp_img_list = []
            for i in range(j):
                temp_img = sprite.subsurface(i * self.size, y * self.hight, self.size, self.hight)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.hight * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, sc_w, sc_h, surface, target):
        speed = 10
        gravity = 2
        dx = 0
        dy = 0

        #получать нажатия клавиш
        key = pygame.key.get_pressed()


        #может выполнять другие действия только в том случае, если в данный момент не атакует
        if self.attacking == False:
            if key[pygame.K_LEFT]:
                dx = -speed
            if key[pygame.K_RIGHT]:
                dx = speed
            # прыгать
            if key[pygame.K_UP] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            # атака
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)
                # определить, какой тип атаки был использован
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 2



        #применение гравитации
        self.vel_y += gravity
        dy += self.vel_y

        #игрок остается на экране
        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > sc_w:
            dx = sc_w - self.rect.right
        if self.rect.bottom + dy > sc_h - 70:
            self.vel_y = 0
            self.jump = False
            dy = sc_h - 70 - self.rect.bottom

        #убедиться, что игроки смотрят друг на друга
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #обновления позиции игрока
        self.rect.x += dx
        self.rect.y += dy

    # обрабатывать обновления анимации
    def update(self):
        time = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > time:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[0] * self.image_scale)))