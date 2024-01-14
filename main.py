import pygame

class Fighter():
    def __init__(self, player, x, y, flip, data, sprite, steps):
        self.player = player
        self.size = data[0]
        self.imagescale = data[1]
        self.offset = data[2]
        self.animationlist = self.images(sprite, steps)
        self.action = 0
        self.frame = 0
        self.update = pygame.time.get_ticks()
        self.image = self.animationlist[self.action][self.frame]
        self.flip = flip
        self.rect = pygame.Rect((x, y, 80, 180))
        self.yspeed = 0
        self.attackingcooldown = 0
        self.jumppossibility = False
        self.attackingtype = 0
        self.attacking = False
        self.xp = 100
        self.running = False
        self.alive = True

    def images(self, sprite, steps):
        animationlist = []
        for y, animation in enumerate(steps):
            temp_img = []
            for i in range(animation):
                temp = sprite.subsurface(i * self.size, y * self.size, self.size, self.size)
                temp_img.append(pygame.transform.scale(temp, (self.size * self.imagescale, self.size * self.imagescale)))
            animationlist.append(temp_img)
        return animationlist

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.imagescale), self.rect.y - (self.offset[1] * self.imagescale)))

    def attack(self, target):
        if self.attackingcooldown == 0:
            self.attacking = True
            attackingrect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            if attackingrect.colliderect(target.rect):
                target.xp -= 10

    def updating(self):
        if self.xp <= 0:
            self.xp = 0
            self.alive = False
            self.update_action(4)
        elif self.attacking is True:
            self.update_action(3)
        elif self.jumppossibility == True:
            self.update_action(2)
        elif self.running == True:
            self.update_action(1)
        else:
            self.update_action(0)
        animationcooldown = 150
        self.image = self.animationlist[self.action][self.frame]
        if pygame.time.get_ticks() - self.update > animationcooldown:
            self.frame += 1
            self.update = pygame.time.get_ticks()
        if self.frame >= len(self.animationlist[self.action]):
            if self.alive == False:
                self.frame = len(self.animationlist[self.action]) - 1
            else:
                self.frame = 0
        if self.action == 3:
            self.attacking = False
            self.attackingcooldown = 20





    def moving(self, surface, target, gameover):
        speed = 8
        xcoor = 0
        ycoor = 0
        grav = 2
        self.running = False
        self.attackingtype = 0
        key = pygame.key.get_pressed()

        if self.attacking is False and self.alive is True and gameover is False:
            if self.player == 1:
                if key[pygame.K_LEFT]:
                    xcoor = -speed
                    self.running = True
                if key[pygame.K_RIGHT]:
                    xcoor = speed
                    self.running = True
                if key[pygame.K_UP] and self.jumppossibility is False:
                    self.yspeed = -30
                    self.jumppossibility = True
                if key[pygame.K_l]:
                    self.attack(target)
                    self.action = 3
            if self.player == 2:
                if key[pygame.K_a]:
                    xcoor = -speed
                    self.running = True
                if key[pygame.K_d]:
                    xcoor = speed
                    self.running = True
                if key[pygame.K_w] and self.jumppossibility is False:
                    self.yspeed = -30
                    self.jumppossibility = True
                if key[pygame.K_r]:
                    self.attack(target)
                    self.action = 3

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

        if self.attackingcooldown > 0:
            self.attackingcooldown -= 1


        self.rect.x += xcoor
        self.rect.y += ycoor

    def update_action(self, newaction):
        if newaction != self.action:
            self.action = newaction
            self.frame = 0
            self.update = pygame.time.get_ticks()


