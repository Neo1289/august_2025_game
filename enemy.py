from symtable import Class

import pygame
import random

class ColorChange:
    def __init__(self):
        self.rgb_dict = {
            1: (45, 125, 255),
            2: (255, 99, 71),
            3: (60, 179, 113),
            4: (255, 206, 84),
            5: (153, 102, 204),
        }

    def get_color(self, number:int):
        return self.rgb_dict.get(number, (255, 255, 255))

class AttributeChange:
    def __init__(self):
        self.changed_x = 0

    def change_position(self,level, y: int):
        self.positive = [1, 2, 3, 4, 5]
        self.negative = [-1, -2, -3, -4, -5]
        self.tuple_ge = (random.choice(self.positive), random.choice(self.negative))
        if level % 3 == 0 and y > 100:
            self.changed_x = random.choice(self.tuple_ge)

class AdditionalGear:
    def __init__(self, x:int, y:int, size:int):
        self.image = pygame.Surface((size, size))
        self.rect = pygame.Rect(x, y, size, size)
        self.image.fill((25, 255, 255))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups: pygame.sprite.Sprite, x: int, y: int, screen: pygame.display, size: int, speed: int, life: int, level: int):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size
        self.enemy = True
        self.image = pygame.Surface((size, size))
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.life = life
        self.level = level
        self.groups = groups

        ####1th class
        self.color_generator = ColorChange()
        self.image.fill(self.color_generator.get_color(self.level))

        if self.level >=1:
        ###2nd class
            self.additional_gear = AdditionalGear(0, 0, self.size)

            gear_x = (self.size - self.additional_gear.rect.width) // 2
            gear_y = self.size - self.additional_gear.rect.height // 2
            self.image.blit(self.additional_gear.image, (gear_x, gear_y))

        ###3rd class
        self.attribute_change = AttributeChange()

    def update_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.y += self.speed

        self.attribute_change.change_position(self.level,self.y)
        self.update_position(self.x + self.attribute_change.changed_x, self.y)

        if self.y > 610:
            self.kill()