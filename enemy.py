import pygame


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

class ShootMissiles:
    def __init__(self):
        ###create a missile rectangle
        pass

    def enemy_shoot(self,number:int):
        if number > 2:
            pass

class Enemy(pygame.sprite.Sprite):
    def __init__(self,groups: pygame.sprite.Sprite, x:int, y:int,screen:pygame.display, size:int,speed:int,life:int,level:int):
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
        #####classes composition
        ####first class
        self.color_generator = ColorChange()
        self.image.fill(self.color_generator.get_color(self.level))
        ####second class
        self.shooting = ShootMissiles()
        self.shooting.enemy_shoot(self.level)

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