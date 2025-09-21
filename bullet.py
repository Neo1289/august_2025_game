import pygame

class GiganticBullet:
    def __init__(self, fruits:int):
        self.fruits = fruits
        self.change_size = 0

    def giga_action(self):
        if self.fruits >= 3:
            self.change_size = self.fruits*5

class Bullet(pygame.sprite.Sprite):
    def __init__(self,groups: pygame.sprite.Sprite, x:int, y:int,screen:pygame.display, size:int,speed:int,rgb:tuple, fruit_taken:int):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.screen = screen
        self.fruit_taken = fruit_taken
        self.giga_bull = GiganticBullet(self.fruit_taken)
        self.giga_bull.giga_action()
        self.size = size + self.giga_bull.change_size
        self.bullet = True
        self.rgb = rgb
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.rgb)
        self.rect = pygame.Rect(x, y, self.size, self.size)
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