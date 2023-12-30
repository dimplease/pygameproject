import pygame

class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)

    def moving(self):
        speed = 8
        xcoor = 0
        ycoor = 0
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            xcoor = -speed
        if key[pygame.K_RIGHT]:
            xcoor = speed

        self.rect.x += xcoor
        self.rect.y += ycoor
