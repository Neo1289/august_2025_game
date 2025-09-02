import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,groups: pygame.sprite.Sprite, x:int, y:int,screen:pygame.display, size:int,speed:int):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size
        self.name = "bullet"
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 255, 0))
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed

    def update_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.y -= self.speed
        self.update_position(self.x, self.y)

        if self.y < 0:
            self.kill()