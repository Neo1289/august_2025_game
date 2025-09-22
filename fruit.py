
import pygame

class ExoticFruit:
    def __init__(self):
        self.rgb_tuple= (45, 125, 255)
        self.doping= 2

    def get_color(self):

        return self.rgb_tuple

    def dope(self):

        return self.doping

class Fruit(pygame.sprite.Sprite):
    def __init__(self, groups: pygame.sprite.Sprite, x: int, y: int, size: int, speed: int,color:tuple,level:int):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.size = size
        self.fruit = True
        self.image = pygame.Surface((size, size))
        self.rect = pygame.Rect(x, y, size, size)
        self.level = level
        self.exotic_fruit = ExoticFruit()
        self.speed = speed
        self.color = color
        self.image.fill(self.color if self.level <2 else self.exotic_fruit.get_color())
        self.potency = 0
        self.potency += self.exotic_fruit.dope() if self.level >= 2 else 0

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