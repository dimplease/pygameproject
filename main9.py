import pygame


class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def move(self, sc_w, sc_h, surface, target):
        speed = 10
        gravity = 2
        dx = 0
        dy = 0

        #получать нажатия клавиш
        key = pygame.key.get_pressed()


        #может выполнять другие действия только в том случае, если в данный момент не атакует
        if self.attacking == False:
            if key[pygame.K_a]:
                dx = -speed
            if key[pygame.K_d]:
                dx = speed
            # прыгать
            if key[pygame.K_w] and self.jump == False:
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


        #обновления позиции игрока
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
