import pygame

class Fighter():
    def __init__(self, x, y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.yspeed = 0
        self.jumppossibility = False
        self.attackoption = 0
        self.attacking = False
        self.xp = 100

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)

    def attack(self, surface, target):
        self.attacking = True
        attackingrect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (255, 0, 0), attackingrect)
        if attackingrect.colliderect(target.rect):
            target.xp -= 10

    def moving(self, surface, target):
        speed = 8
        xcoor = 0
        ycoor = 0
        grav = 2
        key = pygame.key.get_pressed()

        if self.attacking is False:
            if key[pygame.K_LEFT]:
                xcoor = -speed
            if key[pygame.K_RIGHT]:
                xcoor = speed
            if key[pygame.K_UP] and self.jumppossibility is False:
                self.yspeed = -30
                self.jumppossibility = True
            if key[pygame.K_l] or key[pygame.K_k]:
                self.attack(surface, target)
                if key[pygame.K_l]:
                    self.attackoption = 1
                if key[pygame.K_k]:
                    self.attackoption = 2

        self.yspeed += grav
        ycoor += self.yspeed

        if self.rect.left + xcoor < 0:
            xcoor = -self.rect.left
        if self.rect.right + xcoor > 1000:
            xcoor = 1000 - self.rect.right
        if self.rect.bottom + ycoor > 490:
            self.yspeed = 0
            self.jumppossibility = False
            ycoor = 490 - self.rect.bottom

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        self.rect.x += xcoor
        self.rect.y += ycoor
