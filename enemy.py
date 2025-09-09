import pygame
import random

class ColorChange:
    def color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)


class Enemy(pygame.sprite.Sprite):
    def __init__(self,groups: pygame.sprite.Sprite, x:int, y:int,screen:pygame.display, size:int,speed:int,rgb:tuple,life:int):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size
        self.enemy = True
        self.image = pygame.Surface((size, size))
        self.rgb = rgb
        self.image.fill(self.rgb)
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.life = life
        self.color_generator = ColorChange()

    def update_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.y += self.speed
        self.update_position(self.x, self.y)

        if self.y > 603:
            self.kill()